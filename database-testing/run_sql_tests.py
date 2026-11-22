"""Build the synthetic dataset and run the six SQL test cases from the workbook.

Usage:  python run_sql_tests.py
Creates a fresh in-file SQLite database (synthetic_banking.db), loads
schema.sql + seed_data.sql, executes the check query of every case in
queries/, and prints the actual output plus a Pass/Fail verdict per case.
All data is fictional; this never touches the ParaBank database.
"""
import sqlite3
from pathlib import Path

HERE = Path(__file__).parent
DB_PATH = HERE / "synthetic_banking.db"

EXPECTED_TXN_COUNTS = {2001: 3, 2002: 2, 2003: 2, 2004: 2, 2005: 1}


def build_db() -> sqlite3.Connection:
    if DB_PATH.exists():
        DB_PATH.unlink()
    con = sqlite3.connect(DB_PATH)
    con.executescript((HERE / "schema.sql").read_text())
    con.executescript((HERE / "seed_data.sql").read_text())
    return con


def run_case(con: sqlite3.Connection, case_id: str) -> tuple[str, str]:
    rows = con.execute((HERE / "queries" / f"{case_id}.sql").read_text()).fetchall()
    if case_id == "DB-ACCT-001":
        return ("Pass" if rows[0][0] == 0 else "Fail"), f"orphan_accounts = {rows[0][0]}"
    if case_id == "DB-TXN-001":
        actual = {r[0]: r[1] for r in rows}
        ok = actual == EXPECTED_TXN_COUNTS
        return ("Pass" if ok else "Fail"), f"per-account counts = {actual}"
    # Remaining cases pass when the check query returns no violation rows.
    return ("Pass" if not rows else "Fail"), f"violation rows = {rows}"


def main() -> None:
    con = build_db()
    cases = ["DB-ACCT-001", "DB-TRF-001", "DB-TRF-002", "DB-TRF-003", "DB-TXN-001", "DB-AUTH-001"]
    results = []
    for case_id in cases:
        status, detail = run_case(con, case_id)
        results.append(status)
        print(f"{case_id}: {status}  ({detail})")
    print(f"\n{results.count('Pass')} passed, {results.count('Fail')} failed of {len(results)} SQL cases")


if __name__ == "__main__":
    main()
