-- Task about create 3 functions
-- 1th -> return table
-- 2th -> use loops
-- 3th -> use cursor

-- func 1 where return table
-- get customers with orders and cars_id
create or replace function get_customers_by_order_id(id_order int)
    returns table(customer_id int, first_name varchar, last_name varchar, car_id int)
language plpgsql
as $$
    begin
        return query
            SELECT
                customers.id,
                customers.first_name,
                customers.last_name,
                orders.car_id
            FROM customers
            JOIN orders
            ON customers.id = orders.customer_id
            AND orders.id = id_order;
    end;
$$;

-- check this func by order_id -> 14
SELECT * FROM get_customers_by_order_id(id_order := 14);


-- create func with loop
-- This func can send message to all prone like SMS
create or replace function send_message_to_all_numbers(message text)
    returns void
language plpgsql
as $$
DECLARE
    phones record;
BEGIN

    for phones in select phone
	       from address
    loop
        -- in this body we can add something func about real sending sms by all phones
	    raise notice 'Message: <%> sent to phone - % as SMS.', message, phones.phone;
    end loop;
end;
$$;

-- check this MEGA func with sending SMS
SELECT send_message_to_all_numbers(message := 'Without a car? Rent!');


-- func with cursor
-- get all id cars by concrete branch id
create or replace function get_cars_in_branch(branch_id integer)
   returns text
as $$
DECLARE
	 cars_id text default '';
	 rec_cars   record;
	 cursor_cars cursor(id_branch integer)
		 for select
		         car.id
		 from branch
		 LEFT JOIN car
		 ON branch.id = car.branch_id
		 WHERE branch.id = id_branch;
begin
   -- open the cursor and set default text
   open cursor_cars(branch_id);
   cars_id := 'Cars id: ';

   -- run step by step on all cars id
   loop
    -- fetch row into the cars
      fetch cursor_cars into rec_cars;
    -- exit when no more cars
      exit when not found;

        cars_id := cars_id || rec_cars.id || '; ';
   end loop;

   -- close the cursor
   close cursor_cars;
   return cars_id;
end; $$
language plpgsql;

-- check this cursor and get all id cars in concrete branch
select get_cars_in_branch(branch_id := 1);
