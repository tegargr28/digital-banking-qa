-- DB-AUTH-001 (FR-002): usernames are unique in the user store.
-- Expected: no rows (no duplicate usernames).
SELECT username, COUNT(*) AS occurrences
FROM customers
GROUP BY username
HAVING COUNT(*) > 1;
