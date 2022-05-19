-- create two procedures
-- use transactions for insert update etc


-- add new customer and check to real id address in database
create or replace procedure add_new_customer(name_first varchar, name_last varchar, id_address int)
language plpgsql
as $$
begin
    -- insert new user to table user
    INSERT INTO customers (first_name, last_name, address_id)
    VALUES (name_first, name_last, id_address);

    -- check to correct input names
    IF name_first != '' AND name_last != '' THEN
        commit;
    ELSE
        rollback;
    END IF;
end;
$$;

-- check this result
call add_new_customer(name_first := '', name_last := 'Demo', id_address := 1);
SELECT * FROM customers where address_id = 1;


-- procedure about change price car by id and check new price
create or replace procedure change_price_car_by_id(car_id int, new_price int)
language plpgsql
as $$
declare
    min int;
    max int;
begin
    -- range about correct price
    min := 200000;
    max := 5000000;

    -- set new price
    UPDATE car
    SET price = new_price
    WHERE id = car_id;

    -- check changes
    IF min < new_price and new_price < max then
        commit;
    ELSE
        rollback;
    end if;

end;
$$;

-- set new price -> wrong and normal
call change_price_car_by_id(car_id := 1, new_price := 654255);
SELECT * FROM car WHERE id = 1;
