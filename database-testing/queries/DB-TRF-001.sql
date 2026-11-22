-- DB-TRF-001 (FR-004): balance reconciliation.
-- Stored balance must equal opening balance + credits - debits per account.
-- Expected: no rows (no account has a reconciliation difference).
SELECT a.id AS account_id,
       a.balance AS stored_balance,
       a.opening_balance
         + COALESCE(SUM(CASE WHEN t.txn_type = 'Credit' THEN t.amount END), 0)
         - COALESCE(SUM(CASE WHEN t.txn_type = 'Debit'  THEN t.amount END), 0) AS computed_balance
FROM accounts a
LEFT JOIN transactions t ON t.account_id = a.id
GROUP BY a.id
HAVING ABS(stored_balance - computed_balance) > 0.001;
