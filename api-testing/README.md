# API Testing

Exploration and execution evidence for the ParaBank public REST API. Only endpoints that have actually been called are documented; results are recorded in the API Test Cases sheet of `test-cases.xlsx`. Never commit real credentials or tokens — the only account used here is the published public demo account.

## Postman collection

`parabank-api.postman_collection.json` mirrors the workbook's API cases (API-AUTH-001/002, API-ACCT-001..003, API-TRF-001, API-TXN-001, API-SESS-001), each with a basic status/content check.

1. In Postman: **Import** → select the collection file.
2. The collection carries its own variables (`baseUrl`, `username`, `password`, `customerId`, `accountId`, `toAccountId`) — no separate environment is required.
3. Run **API-AUTH-001** first. Demo data resets periodically, so if login fails or IDs differ, refresh `customerId` / `accountId` / `toAccountId` from a fresh login and account list before running the dependent requests.

## Execution record (summary)

| Session | Scope | Result |
|---|---|---|
| EXEC-001 (2026-11-23) | API-AUTH-001/002, API-ACCT-001..003 via curl | All Pass |
| EXEC-006 (2026-11-23) | API-TXN-001, API-SESS-001, API-TRF-001 via curl | All Pass — transfer verified by balance deltas of exactly 10.00 on both accounts |

Note from EXEC-006: a same-day re-check of API-AUTH-001 returned HTTP 400 because the public demo data had changed (see Risk RSK-101 in `docs/risk-assessment.md`). The original EXEC-001 result stands for its execution time; re-run the login request to obtain the current demo state before dependent requests.

Known related defect: the **web UI** login accepts an invalid password (BUG-001, Critical, Open) while this API rejects it correctly — see the Bug Reports sheet in `test-cases.xlsx`.
