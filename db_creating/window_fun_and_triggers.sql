-- Tasks about Window Funcs and Triggers

-- window func about get avg by categories
CREATE OR REPLACE VIEW products_with_avg AS
SELECT
    category_title,
    product_title,
    price,
    ROUND(AVG(price)
    OVER(PARTITION BY category_title))
FROM products
INNER JOIN categories
USING (category_id);

-- show current result with win fun
SELECT * FROM products_with_avg;


-- next tasks about triggers --


-- this table contains info about changed total in orders
CREATE TABLE order_changed (
   id INT GENERATED ALWAYS AS IDENTITY,
   order_id INT NOT NULL,
   old_total NUMERIC NOT NULL,
   new_total NUMERIC NOT NULL,
   changed_on TIMESTAMP(6) NOT NULL
);

-- this trigger works if total in table orders was changed
CREATE OR REPLACE FUNCTION new_update()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS $$
BEGIN
    IF NEW.total != OLD.total AND new.total > 0 THEN
        -- set time updates
         INSERT INTO order_changed(order_id, old_total, new_total, changed_on)
		 VALUES(old.order_id, old.total, new.total, now());
    END IF;
    RETURN NEW;
END;
$$;

-- get new trigger
BEGIN;
DROP TRIGGER IF EXISTS before_change_total ON shop.public.orders;
-- add trigger for orders
CREATE TRIGGER before_change_total
BEFORE UPDATE
ON orders
FOR EACH ROW
EXECUTE PROCEDURE new_update();
COMMIT;

-- check this order
SELECT * FROM orders where order_id = 1;
-- change total
UPDATE orders
SET total = 150
WHERE order_id = 1;
-- check result
SELECT * FROM order_changed;


-- next trigger --

SELECT * FROM categories;

-- add trigger for categories ..
-- .. in situation if insert new category --
CREATE TRIGGER before_add_category
BEFORE INSERT
ON categories
FOR EACH ROW
EXECUTE PROCEDURE check_add();

-- this trigger works if add new category is correct
CREATE OR REPLACE FUNCTION check_add()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS $$
BEGIN
    -- return normal trigger if data is correct
    IF NEW.category_title IS NOT NULL THEN
        RETURN NEW;
    ELSE
        RETURN NULL;
    END IF;
END;
$$;

-- add new category to table categories
CREATE OR REPLACE PROCEDURE add_category(id integer, title varchar, description text)
LANGUAGE PLPGSQL
AS $$
BEGIN
    -- pre update user number
    INSERT INTO categories (category_id, category_title, category_description)
    VALUES (id, title, description);

    -- check about correct
    IF description != '' THEN
         COMMIT;
      ELSE ROLLBACK;
    END IF;

END;
$$;

-- check result
SELECT * FROM categories;
-- in this situation trigger not accepted insert
CALL add_category(22, 'Category 22', '');
-- normal insert with work trigger
CALL add_category(40, 'Category 40', 'Category 40 description.');
