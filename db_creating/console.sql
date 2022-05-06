CREATE DATABASE shop;

CREATE TABLE users
(
  user_id INT UNIQUE,
  email VARCHAR(255),
  password VARCHAR(255),
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  middle_name VARCHAR(255),
  is_staff INT,
  country VARCHAR(255),
  city VARCHAR(255),
  address TEXT
);

COPY users FROM '/usr/src/users.csv' WITH (FORMAT csv);

CREATE TABLE carts
(
  cart_id INT UNIQUE,
  Users_user_id INT REFERENCES users(user_id),
  subtotal DECIMAL,
  total DECIMAL,
  timestamp TIMESTAMP(2)
);

COPY carts FROM '/usr/src/carts.csv' WITH (FORMAT csv);

CREATE TABLE order_status
(
  order_status_id INT UNIQUE,
  status_name VARCHAR(255)
);

COPY order_status FROM '/usr/src/order_statuses.csv' WITH (FORMAT csv);

CREATE TABLE orders
(
    order_id INT UNIQUE,
    Carts_cart_id INT REFERENCES carts(cart_id),
    Order_status_order_status_id INT REFERENCES order_status(order_status_id),
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2)
);

COPY orders FROM '/usr/src/orders.csv' WITH (FORMAT csv);

CREATE TABLE categories
(
  category_id INT UNIQUE,
  category_title VARCHAR(255),
  category_description TEXT
);

COPY categories FROM '/usr/src/categories.csv' WITH (FORMAT csv);

CREATE TABLE products
(
  product_id INT UNIQUE,
  product_title VARCHAR(255),
  product_description TEXT,
  in_stock INT,
  price FLOAT,
  slug VARCHAR(45),
  category_id INT REFERENCES categories(category_id)
);

COPY products FROM '/usr/src/products.csv' WITH (FORMAT csv);

CREATE TABLE cart_product
(
  carts_cart_id INT REFERENCES carts(cart_id),
  products_product_id INT REFERENCES products(product_id)
);

COPY cart_product FROM '/usr/src/cart_products.csv' WITH (FORMAT csv);

-- change something tables

ALTER TABLE users
ADD COLUMN phone_number INT;

ALTER TABLE users
ALTER COLUMN phone_number TYPE VARCHAR;

-- We decided to become businessmen ...
-- ... and double our prices!

UPDATE products
SET price = price * 2;
