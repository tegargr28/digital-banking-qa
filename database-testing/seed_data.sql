-- Synthetic banking dataset - seed data (all people and values are fictional)
--
-- Transfers seeded (each posts one Debit and one Credit of equal amount):
--   TRF-9001  account 2001 -> 2002   200.00
--   TRF-9002  account 2003 -> 2004   125.50
--   TRF-9003  account 2004 -> 2005   300.00
--   TRF-9004  account 2002 -> 2001    50.25
--   TRF-9005  account 2001 -> 2003    75.00
--
-- Expected transaction counts per account (used by DB-TXN-001):
--   2001: 3   2002: 2   2003: 2   2004: 2   2005: 1
--
-- Stored balances equal opening_balance + credits - debits for every account:
--   2001: 1500.00 - 200.00 + 50.25 - 75.00 = 1275.25
--   2002: 3200.00 + 200.00 - 50.25         = 3349.75
--   2003:  875.50 - 125.50 + 75.00         =  825.00
--   2004: 2100.00 + 125.50 - 300.00        = 1925.50
--   2005:  500.00 + 300.00                 =  800.00

INSERT INTO customers (id, first_name, last_name, username, city, zip_code) VALUES
    (1001, 'Amelia', 'Hart',   'amelia.hart',   'Springfield', '01101'),
    (1002, 'Brian',  'Cole',   'brian.cole',    'Riverton',    '82501'),
    (1003, 'Clara',  'Nguyen', 'clara.nguyen',  'Lakewood',    '80215');

INSERT INTO accounts (id, customer_id, account_type, opening_balance, balance) VALUES
    (2001, 1001, 'CHECKING', 1500.00, 1275.25),
    (2002, 1001, 'SAVINGS',  3200.00, 3349.75),
    (2003, 1002, 'CHECKING',  875.50,  825.00),
    (2004, 1003, 'CHECKING', 2100.00, 1925.50),
    (2005, 1003, 'SAVINGS',   500.00,  800.00);

INSERT INTO transactions (id, account_id, transfer_ref, txn_type, amount, description, txn_date) VALUES
    ( 1, 2001, 'TRF-9001', 'Debit',  200.00, 'Funds Transfer Sent',     '2026-11-20'),
    ( 2, 2002, 'TRF-9001', 'Credit', 200.00, 'Funds Transfer Received', '2026-11-20'),
    ( 3, 2003, 'TRF-9002', 'Debit',  125.50, 'Funds Transfer Sent',     '2026-11-20'),
    ( 4, 2004, 'TRF-9002', 'Credit', 125.50, 'Funds Transfer Received', '2026-11-20'),
    ( 5, 2004, 'TRF-9003', 'Debit',  300.00, 'Funds Transfer Sent',     '2026-11-21'),
    ( 6, 2005, 'TRF-9003', 'Credit', 300.00, 'Funds Transfer Received', '2026-11-21'),
    ( 7, 2002, 'TRF-9004', 'Debit',   50.25, 'Funds Transfer Sent',     '2026-11-21'),
    ( 8, 2001, 'TRF-9004', 'Credit',  50.25, 'Funds Transfer Received', '2026-11-21'),
    ( 9, 2001, 'TRF-9005', 'Debit',   75.00, 'Funds Transfer Sent',     '2026-11-22'),
    (10, 2003, 'TRF-9005', 'Credit',  75.00, 'Funds Transfer Received', '2026-11-22');
