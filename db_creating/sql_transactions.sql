-- 1st work with some table
-- Start transaction
BEGIN;
-- insert new person to customers
INSERT INTO potential_customers
VALUES(101,
       'general@gmail.com',
       'Oleksii',
       'Rubel',
       'General',
       'Kharkiv');
-- create new savepoint after insert
SAVEPOINT after_insert;
-- change this user
UPDATE potential_customers
SET second_name='BOSS'
WHERE surname='Rubel';
-- again create savepoint
SAVEPOINT after_update;
-- delete this user -_-
DELETE FROM potential_customers
WHERE id=101;
-- check to table
SELECT * FROM potential_customers;
-- return boss
ROLLBACK TO SAVEPOINT after_update;
-- end transaction
COMMIT;

-- 2d work with next table
-- start transaction
BEGIN;
-- check this table
SELECT * FROM order_status;
-- set default savepoint
SAVEPOINT default_table;
-- add new property
ALTER TABLE order_status
ADD status_time TIME;
-- check
SELECT * FROM order_status;
-- rollback to default table
ROLLBACK TO SAVEPOINT default_table;
-- check
SELECT * FROM order_status;
-- end this transaction
COMMIT;

-- 3d work with next table
-- start transaction
BEGIN;
-- check this table
SELECT product_title, price
FROM products
ORDER BY price DESC;
-- set default savepoint
SAVEPOINT default_prices;
-- up all price to x4
UPDATE products
SET price = price * 4;
-- check this nice prices
SELECT product_title, price
FROM products
WHERE price > 400
ORDER BY price DESC;
-- get default prices
ROLLBACK TO SAVEPOINT default_prices;
-- check
SELECT product_title, price
FROM products
ORDER BY price DESC;
-- end transaction
COMMIT;
