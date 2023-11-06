CREATE SCHEMA Bank;
USE Bank

CREATE TABLE Customers (
    customer_id INT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    PRIMARY KEY (customer_id)
);

CREATE TABLE Accounts (
    accounts_id INT,
    Balance INT NOT NULL,
    customer_id INT,
    PRIMARY KEY (accounts_id),
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

CREATE TABLE Transactions (
    transactions_id INT,
    accounts_id INT,
    amount INT NOT NULL,
    PRIMARY KEY (transactions_id),
    FOREIGN KEY (accounts_id) REFERENCES Accounts (accounts_id)
);

INSERT INTO Customers VALUES (22, "sdaegh ghasemi", 225, "909 907 1209");
INSERT INTO Customers VALUES (24, "barsa bordbar", 21, "8*");

INSERT INTO Accounts VALUES (102, 750, 22);
INSERT INTO Accounts VALUES (104, 750, 24);

INSERT INTO Transactions VALUES (1, 102, 20);
INSERT INTO Transactions VALUES (2, 102, -40);
INSERT INTO Transactions VALUES (3, 104, 200);

SELECT * FROM Customers;
SELECT * FROM Accounts;
SELECT * FROM Transactions;

/* khorogi
/*----------------------------------------------------------------
+-------------+----------------+-----+----------------+
| customer_id | name           | age | contact_number |
+-------------+----------------+-----+----------------+
|          22 | sdaegh ghasemi | 225 | 909 907 1209   |
|          24 | barsa bordbar  |  21 | 8*             |
+-------------+----------------+-----+----------------+
2 rows in set (0.00 sec)

+-------------+---------+-------------+
| accounts_id | Balance | customer_id |
+-------------+---------+-------------+
|         102 |     750 |          22 |
|         104 |     750 |          24 |
+-------------+---------+-------------+
2 rows in set (0.00 sec)

+-----------------+-------------+--------+
| transactions_id | accounts_id | amount |
+-----------------+-------------+--------+
|               1 |         102 |     20 |
|               2 |         102 |    -40 |
|               3 |         104 |    200 |
+-----------------+-------------+--------+
----------------------------------------------------------------*/
