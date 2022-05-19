-- add two triggers
-- before and after operations
-- and funcs for this triggers


-- this trigger works orders days was changed and then set new date update
CREATE OR REPLACE FUNCTION new_update()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS $$
BEGIN
    -- check about update days in orders
    IF NEW.days != OLD.days AND NEW.days > 0 THEN
        NEW.date = now();
    END IF;
    RETURN NEW;
END;
$$;

-- add trigger for orders
CREATE TRIGGER before_change_total
BEFORE UPDATE
ON orders
FOR EACH ROW
EXECUTE PROCEDURE new_update();

-- update days
UPDATE orders
SET days = 14
WHERE id = 1;
-- check this trigger
SELECT * FROM orders
WHERE id = 1;


-- trigger about send SMS after change price to concrete car

-- func for trigger after update car price
CREATE OR REPLACE FUNCTION new_update_price()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS $$
declare
    min int;
    max int;
    phone_customer varchar;
begin

    -- get customer phone
    phone_customer = get_number_customer_by_car_id(id_car := NEW.id);

    -- range about correct price
    min := 200000;
    max := 5000000;

    -- check about update price
    IF NEW.price != OLD.price AND
       NEW.price > min AND
       NEW.price < max
    THEN
        raise notice 'Message: < Price for car [id -> %] was changed at % sent to number - % >', NEW.id,
                                                                                                 NEW.price,
                                                                                                 phone_customer;
    ELSE
        RETURN NULL;
    END IF;

    RETURN NEW;
END;
$$;

-- by this func we can get phone customer by id car
CREATE OR REPLACE FUNCTION get_number_customer_by_car_id(id_car int)
    returns varchar
language plpgsql
as $$
DECLARE
    phone varchar;
BEGIN
    -- get customer phone
    SELECT address.phone
    FROM car
    JOIN orders
    ON car.id = orders.car_id
    JOIN customers
    ON orders.customer_id = customers.id
    JOIN address
    ON customers.address_id = address.id
    WHERE car.id = id_car
    INTO phone;

    return phone;
END;
$$;

-- add trigger for car if price is changed
CREATE TRIGGER before_change_total
AFTER UPDATE
ON car
FOR EACH ROW
EXECUTE PROCEDURE new_update_price();

-- update price
UPDATE car
SET price = 900000
WHERE id = 1;

-- check this change by price on car
SELECT * FROM car WHERE id = 1;

-- after this changed customer give a SMS about this change price on car
