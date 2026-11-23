-- Synthetic banking dataset - schema (SQLite)
-- Fictional data only, created for SQL testing practice.
-- This is NOT the ParaBank database; ParaBank does not expose its database.

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id         INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name  TEXT NOT NULL,
    username   TEXT NOT NULL,
    city       TEXT,
    zip_code   TEXT
);

CREATE TABLE accounts (
    id              INTEGER PRIMARY KEY,
    customer_id     INTEGER NOT NULL REFERENCES customers(id),
    account_type    TEXT NOT NULL CHECK (account_type IN ('CHECKING', 'SAVINGS')),
    opening_balance NUMERIC NOT NULL,
    balance         NUMERIC NOT NULL
);

CREATE TABLE transactions (
    id           INTEGER PRIMARY KEY,
    account_id   INTEGER NOT NULL REFERENCES accounts(id),
    transfer_ref TEXT,
    txn_type     TEXT NOT NULL CHECK (txn_type IN ('Debit', 'Credit')),
    amount       NUMERIC NOT NULL CHECK (amount > 0),
    description  TEXT,
    txn_date     TEXT NOT NULL
);
