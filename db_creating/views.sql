-- Task about 3 view for:
-- 1) products
-- 2) order_status and order
-- 3) products and category
-- And create materialize view for heavy select (3)
-- Examples and delete this views
--
-- this view about product, count in stock and price once
CREATE VIEW top_products AS
SELECT product_title, in_stock, price
FROM products
WHERE products.in_stock > 40
AND products.price > 300
ORDER BY products.price DESC
LIMIT 100;
-- check this view about all price for every product
SELECT product_title, price*in_stock AS all_price
FROM top_products
ORDER BY product_title;
-- delete this view
DROP VIEW top_products;
--
-- next view about top orders with status names + desc
--
CREATE VIEW top_orders AS
SELECT order_id, total, status_name
FROM orders
INNER JOIN order_status
ON orders.order_status_order_status_id = order_status.order_status_id
ORDER BY total DESC
LIMIT 1000;
-- get top orders - canceled
SELECT * FROM top_orders
WHERE status_name='Canceled'
LIMIT 10;
-- delete this view
DROP VIEW top_orders;
--
-- next materialized view about profit middle products about price
-- EXPLAIN ANALYSE
CREATE MATERIALIZED VIEW product_profit AS
SELECT product_title, in_stock*price AS full_price_in_stock, products.category_id
FROM products
INNER JOIN categories
ON products.category_id = categories.category_id
AND products.category_id = 20
WHERE price > 100 AND price < 400
ORDER BY full_price_in_stock DESC
LIMIT 100;
-- check this view every day and check middle price about products
SELECT ROUND(SUM(full_price_in_stock)) AS all_price
FROM product_profit;
-- delete this view
DROP MATERIALIZED VIEW product_profit;
