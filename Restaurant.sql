CREATE DATABASE Restaurant;

USE Restaurant;

CREATE TABLE Menu (
    menu_id INT AUTO_INCREMENT,
    item_name VARCHAR(50),
    price INT,
    PRIMARY KEY (menu_id));

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    contact_number VARCHAR(15),
    PRIMARY KEY (customer_id)
);

CREATE TABLE Tables (
    table_id INT AUTO_INCREMENT,
    capacity INT,
    PRIMARY KEY (table_id)
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT,
    customer_id INT,
    table_id INT,
    order_time TIMESTAMP,
    PRIMARY KEY (order_id),
    FOREIGN KEY (table_id) REFERENCES Tables(table_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

INSERT INTO Menu VALUES (1, "غذای شماره یک", 200);
INSERT INTO Menu(item_name, price ) VALUES ("غذای شماره دو", 400);

INSERT INTO Customers VALUES (100, "صادق", NULL, "1234567890");
INSERT INTO Customers (first_name, last_name, contact_number) VALUES ("اسماعیل", "قاسمی", "0987654321");

INSERT INTO Tables VALUES (1,2);
INSERT INTO Tables (capacity) VALUES (1);

INSERT INTO Orders VALUES (1000, 100, 1,  '2001-01-09 01:05:01');
INSERT INTO Orders (customer_id, table_id, order_time) VALUES (101, 1, '2001-01-09 01:07:01');
INSERT INTO Orders (customer_id, table_id, order_time) VALUES (101, 2, Null);

SELECT * FROM Menu;
SELECT * FROM Customers;
SELECT * FROM Tables;
SELECT * FROM Orders;

/* khorogi
/*----------------------------------------------------------------
+---------+---------------+-------+
| menu_id | item_name     | price |
+---------+---------------+-------+
|       1 | ???? ????? ?? |   200 |
|       2 | ???? ????? ?? |   400 |
|       3 | ???? ????? ?? |   400 |
+---------+---------------+-------+
3 rows in set (0.00 sec)

+-------------+------------+-----------+----------------+
| customer_id | first_name | last_name | contact_number |
+-------------+------------+-----------+----------------+
|         100 | ????       | NULL      | 1234567890     |
|         101 | ???????    | ?????     | 0987654321     |
|         102 | ???????    | ?????     | 0987654321     |
+-------------+------------+-----------+----------------+
3 rows in set (0.00 sec)

+----------+----------+
| table_id | capacity |
+----------+----------+
|        1 |        2 |
|        2 |        1 |
|        3 |        1 |
+----------+----------+
3 rows in set (0.00 sec)

+----------+-------------+----------+---------------------+
| order_id | customer_id | table_id | order_time          |
+----------+-------------+----------+---------------------+
|     1000 |         100 |        1 | 2001-01-09 01:05:01 |
|     1001 |         101 |        1 | 2001-01-09 01:07:01 |
|     1002 |         101 |        2 | NULL                |
|     1003 |         101 |        1 | 2001-01-09 01:07:01 |
|     1004 |         101 |        2 | NULL                |
+----------+-------------+----------+---------------------+
5 rows in set (0.00 sec)

----------------------------------------------------------------*/
