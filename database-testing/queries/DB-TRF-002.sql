-- DB-TRF-002 (FR-004): every transfer posts exactly one debit and one credit
-- of equal amount (signed sum per transfer = 0, leg count = 2).
-- Expected: no rows (no unbalanced or partially posted transfer).
SELECT transfer_ref,
       COUNT(*) AS legs,
       SUM(CASE WHEN txn_type = 'Credit' THEN amount ELSE -amount END) AS signed_sum
FROM transactions
WHERE transfer_ref IS NOT NULL
GROUP BY transfer_ref
HAVING legs <> 2 OR ABS(signed_sum) > 0.001;
