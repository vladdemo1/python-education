-- Task 1
-- show all users
SELECT * FROM users;
-- show all products
SELECT * FROM products;
-- shoe all order statuses
SELECT * FROM order_status;

-- Task 2
-- show all orders where order paid, finished
SELECT * FROM orders
WHERE order_status_order_status_id = 3
OR order_status_order_status_id = 4;

-- Task 3
-- products price in diapason
SELECT * FROM products
WHERE price > 80.00
AND price <= 150.00;
-- orders after 01.10.2020
SELECT * FROM orders
WHERE created_at > '2020-10-01 00:00:00.00';
-- first of period in 2020
SELECT * FROM orders
WHERE created_at BETWEEN '2020-01-01 00:00:00.00'
AND '2020-06-30 23:59:59.59';
-- products in category 7, 11, 18
SELECT * FROM products
WHERE category_id IN (7, 11, 18);
-- unfinished orders to 31.12.2020
SELECT * FROM orders
WHERE created_at <= '2020-12-31 23:59:59.59'
AND order_status_order_status_id = 2;
-- all orders no created
SELECT * FROM orders
WHERE order_status_order_status_id = 1;

-- Task 4
-- avg all finished orders
SELECT AVG(total) FROM orders
WHERE order_status_order_status_id = 4;
-- maximum sum order in 3th 2020
SELECT MAX(total) FROM orders
WHERE created_at BETWEEN '2020-07-01 00:00:00.00'
AND '2020-12-31 23:59:59.59';