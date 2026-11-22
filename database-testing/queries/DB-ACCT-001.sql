-- DB-ACCT-001 (FR-003): every account references an existing customer.
-- Expected: 0 orphan accounts.
SELECT COUNT(*) AS orphan_accounts
FROM accounts a
LEFT JOIN customers c ON c.id = a.customer_id
WHERE c.id IS NULL;
