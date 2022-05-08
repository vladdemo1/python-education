-- Task 1
-- Zad: create new table potential_customers
CREATE TABLE potential_customers
(
  id INT UNIQUE,
  email VARCHAR(255),
  name VARCHAR(255),
  surname VARCHAR(255),
  second_name VARCHAR(255),
  city VARCHAR(255)
);
-- Zad: fulling current table
COPY potential_customers FROM '/usr/src/potential_customers.csv' WITH (FORMAT csv);
-- Zad: get names and email general from this ...
-- .... potential customers and real customers from city 17
SELECT users.first_name, users.email, potential_customers.name, potential_customers.email
FROM potential_customers
INNER JOIN users
ON TRUE
WHERE users.city = 'city 17';

-- Task 2
-- Zad: get sorted names and emails from table -> users
SELECT first_name, email
FROM users
ORDER BY city, first_name;

-- Task 3
-- Zad: name group and sum count products in current group
SELECT c.category_title, SUM(p.in_stock)
FROM products p, categories c
WHERE p.category_id = c.category_id
GROUP BY c.category_title
ORDER BY SUM(p.in_stock) DESC;

-- Task 4
-- Zad 1 (all products who no contains in something carts)
SELECT p.product_title
FROM cart_product c
RIGHT JOIN products p
ON c.products_product_id = p.product_id
WHERE c.products_product_id IS NULL;
-- Zad 2 (all products no in all order)
SELECT p.product_title
FROM orders o, cart_product c
RIGHT JOIN products p
ON p.product_id = c.products_product_id
WHERE o.carts_cart_id = c.carts_cart_id
GROUP BY p.product_title
ORDER BY p.product_title;
-- Zad 3 (top-10 prods in carts usually)
SELECT p.product_title, COUNT(cp.products_product_id) AS count_in_carts
FROM cart_product cp, products p
WHERE p.product_id = cp.products_product_id
GROUP BY p.product_title, cp.products_product_id
HAVING COUNT (cp.products_product_id) > 0
ORDER BY COUNT(cp.products_product_id) DESC
LIMIT 10;
-- Zad 4 (top-10 prods not only in carts, but and in orders)
SELECT p.product_title
FROM cart_product c, products p
LEFT JOIN orders o
ON o.carts_cart_id = carts_cart_id
WHERE p.product_id = c.products_product_id
GROUP BY c.products_product_id, p.product_title
HAVING COUNT(c.products_product_id) > 0
ORDER BY COUNT(c.products_product_id) DESC
LIMIT 10;
-- Zad 5 (top-5 users max costs to out $ (its total in order))
SELECT u.first_name, SUM(o.total) AS money_spent
FROM orders o, carts c, users u
WHERE o.carts_cart_id = c.cart_id AND c.users_user_id = u.user_id
GROUP BY u.first_name, o.total
ORDER BY SUM(o.total) DESC  -- sum
LIMIT 5;
-- Zad 6 (top-5 users about count orders)
SELECT u.first_name, COUNT(c.users_user_id) as count_orders
FROM users u, carts c
WHERE u.user_id = c.users_user_id
GROUP BY u.first_name
ORDER BY COUNT(c.users_user_id) DESC
LIMIT 5;
-- Zad 7 (top-5 users, who create carts but no order)
SELECT u.first_name
FROM carts c
LEFT JOIN orders o
ON c.cart_id = o.carts_cart_id
INNER JOIN users u
ON c.users_user_id = u.user_id
WHERE o.carts_cart_id IS NULL AND u.user_id = c.users_user_id
GROUP BY u.first_name
ORDER BY COUNT(c.cart_id) DESC
LIMIT 5;