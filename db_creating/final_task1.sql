-- create new data base
CREATE DATABASE rent_car;

-- (1) table about address
CREATE TABLE address
(
  id SERIAL PRIMARY KEY,
  phone VARCHAR(255)
);

-- Insert something info to table address
do $$
begin
   for i in 1..15000 loop
	    INSERT INTO address (phone) VALUES (md5(random()::text));
   end loop;
end; $$;

-- (2) table about home
CREATE TABLE home(
  id SERIAL PRIMARY KEY,
  number_home INT,
  address_id INT REFERENCES address(id)
);

-- Insert something info to table home
do $$
begin
   for i in 1..15000 loop
	    INSERT INTO home (number_home, address_id) VALUES (i, i);
   end loop;
end; $$;

-- (3) table about street
CREATE TABLE street(
  id SERIAL PRIMARY KEY,
  street VARCHAR(255),
  home_id INT REFERENCES home(id)
);

-- Insert something info to table street
do $$
begin
   for i in 1..15000 loop
	    INSERT INTO street (street, home_id) VALUES ('Street ' || i::varchar, i);
   end loop;
end
$$;

-- (4) table about city
CREATE TABLE city(
  id SERIAL PRIMARY KEY,
  city VARCHAR(255),
  street_id INT REFERENCES street(id)
);

-- Insert something info to table city
do $$
begin
   for i in 1..15000 loop
	    INSERT INTO city (city, street_id) VALUES ('City ' || i::varchar, i);
   end loop;
end
$$;

-- (5) table about customers
CREATE TABLE customers(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  address_id INT REFERENCES address(id)
);

-- Insert something info to table city
do $$
begin
   for i in 1..15000 loop
	    INSERT INTO customers (first_name, last_name, address_id)
	    VALUES ('First Name ' || i::varchar, 'Last Name ' || i::varchar , i);
   end loop;
end
$$;

-- (6) create table about branch
CREATE TABLE branch(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  address_id INT REFERENCES address(id)
);

-- Insert something info to table branch
do $$
begin
   for i in 1..15000 loop
	    INSERT INTO branch (name, address_id) VALUES ('Branch Name ' || i::varchar , i);
   end loop;
end
$$;

-- (7) create table about car
CREATE TABLE car(
  id SERIAL PRIMARY KEY,
  price INT,
  number VARCHAR(255),
  branch_id INT REFERENCES branch(id)
);

-- Insert something info to table branch
-- set prise in range 200_000 -> 5_000_000
do $$
begin
   for i in 1..15000 loop
	    INSERT INTO car (price, number, branch_id)
	    VALUES (random()*(5000000 - 200000)+200000, md5(random()::text) , i);
   end loop;
end
$$;

-- (8) create table about order
CREATE TABLE orders(
  id SERIAL PRIMARY KEY,
  date TIMESTAMP(6),
  days INT,
  car_id INT REFERENCES car(id),
  customer_id INT REFERENCES customers(id)
);

-- Insert something info to table orders
-- random days in range 1 -> 31
do $$
begin
   for i in 1..15000 loop
	    INSERT INTO orders (date, days, car_id, customer_id)
	    VALUES (now(), random()*(31 - 1)+1, i , i);
   end loop;
end
$$;

-- (9) create table about producer_car
CREATE TABLE producer_car(
  id SERIAL PRIMARY KEY,
  producer VARCHAR(255),
  car_id INT REFERENCES car(id)
);

-- Insert something info to table producer_car
do $$
begin
   for i in 1..15000 loop
	    INSERT INTO producer_car (producer, car_id) VALUES ('Producer ' || i::varchar , i);
   end loop;
end
$$;

-- (10) create table about model_car
CREATE TABLE model_car(
  id SERIAL PRIMARY KEY,
  model VARCHAR(255),
  producer_car_id INT REFERENCES producer_car(id)
);

-- Insert something info to table model_car
do $$
begin
   for i in 1..15000 loop
	    INSERT INTO model_car (model, producer_car_id) VALUES ('Model ' || i::varchar , i);
   end loop;
end
$$;
