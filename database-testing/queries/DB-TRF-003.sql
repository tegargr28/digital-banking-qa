-- DB-TRF-003 (FR-004): duplicate transaction posting check.
-- Expected: no rows (the same leg of a transfer is never posted twice).
SELECT transfer_ref, account_id, txn_type, COUNT(*) AS postings
FROM transactions
WHERE transfer_ref IS NOT NULL
GROUP BY transfer_ref, account_id, txn_type
HAVING COUNT(*) > 1;
