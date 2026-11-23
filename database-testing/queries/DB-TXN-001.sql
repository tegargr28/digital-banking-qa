-- DB-TXN-001 (FR-006): transaction history completeness per account.
-- Compare with the expected activity documented in seed_data.sql:
--   2001: 3   2002: 2   2003: 2   2004: 2   2005: 1
SELECT account_id, COUNT(*) AS transaction_count
FROM transactions
GROUP BY account_id
ORDER BY account_id;
