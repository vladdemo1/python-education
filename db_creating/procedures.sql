-- create func, set shipping_total = 0 in table order if city == x
-- and return SUM all orders about field shipping_total

-- func about get sum shipping total and then set 0 in this positions
create or replace function get_reset_shipping_by_city(city_name varchar)
returns integer
language plpgsql
AS
$$
DECLARE
    all_sum decimal;
BEGIN

    -- get sum shipping where city = city_name
    SELECT SUM(shipping_total)
    FROM get_info_by_city_name(city_name)
    INTO all_sum;

    -- set zero to selected orders
    IF all_sum IS NOT NULL THEN
        CALL set_zero(city_name);
    END IF;

    -- get this sum
    RETURN all_sum;
END;
$$;

-- create procedure about set sipping total -> 0
create or replace procedure set_zero(city_name varchar)
language plpgsql
as $$
begin
    UPDATE orders
    SET shipping_total = 0
    WHERE orders.carts_cart_id = (SELECT cart_id FROM get_info_by_city_name(city_name));
end;$$;

-- universal func about get current field for main func
create or replace function get_info_by_city_name(city_name varchar)
    returns table(shipping_total decimal, cart_id integer)
language plpgsql
as $$
BEGIN
    return query
        SELECT orders.shipping_total, carts.cart_id
        FROM orders
        JOIN carts
        ON orders.carts_cart_id = carts.cart_id
        JOIN users
        ON carts.users_user_id = users.user_id
        AND users.city = city_name;
end;
$$;

-- Check result
SELECT * FROM  get_reset_shipping_by_city(city_name := 'city 2');
SELECT * FROM orders WHERE shipping_total = 0;

-- 3 procedures

-- add phone to concrete user by id if number is null
create or replace procedure add_phone(id_user integer, phone varchar)
language plpgsql
as $$
DECLARE
    real_number varchar;
BEGIN
    -- get current number
    SELECT phone_number
    FROM users
    WHERE user_id = id_user
    INTO real_number;

    -- pre update user number
    UPDATE users
    SET phone_number = phone
    WHERE users.user_id = id_user;

    -- check state number
    if real_number is null
        then commit;
    else rollback;
    end if;

end;
$$;
-- add and check result
call add_phone(id_user := 2, phone := '0974442255');
SELECT * FROM users WHERE phone_number is not null;


-- change price product to low by percent if count in stock like parameter
create or replace procedure change_price_for_products(count_in_stock integer, percent integer)
language plpgsql
as $$
declare
    f record;
begin
    -- check current percent
    if percent <= 0 or percent >= 100 then
        raise exception 'Bad value for percent!';
    end if;

    -- this for used about show work this loop
    for f in select product_id, in_stock
	       from products
           where in_stock = count_in_stock
    loop
	    UPDATE products
            SET price = price * (100 - percent) * 0.01
        WHERE product_id = f.product_id;
    end loop;
    commit;
end;
$$;
-- check this result
call change_price_for_products(count_in_stock := 0, percent := 25);
SELECT * FROM products WHERE in_stock = 0;


-- change phone with password verify
create or replace procedure change_phone_by_password(id_user integer, new_phone varchar, secret_password varchar)
language plpgsql
as $$
DECLARE
    real_pass varchar;
BEGIN
    UPDATE users
    SET phone_number = new_phone
    WHERE user_id = id_user;

    -- get current user password
    SELECT password
    FROM users
    WHERE user_id = id_user
    INTO real_pass;

    -- check input password with real
    if real_pass = secret_password
        then commit;
    else rollback;
    end if;
END;
$$;

-- check result
call change_phone_by_password(id_user := 1, new_phone := '7783322', secret_password := '84204057691');
SELECT * FROM users where user_id = 1;
