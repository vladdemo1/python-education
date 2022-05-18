-- 3 views (1 view is a materialize)

-- view about concrete info customer and his order
CREATE MATERIALIZED VIEW customer_info AS
    SELECT
        customers.first_name,
        customers.last_name,
        address.phone,
        city.city,
        street.street,
        home.number_home,
        orders.id as order_id
    FROM customers
    JOIN orders
    ON customers.id = orders.customer_id
    JOIN address
    ON customers.address_id = address.id
    JOIN home
    ON address.id = home.address_id
    JOIN street
    ON home.id = street.home_id
    JOIN city
    ON street.id = city.street_id;

-- check this view
EXPLAIN ANALYZE SELECT * FROM customer_info;

-- ....:::: COST WITHOUT MATERIALIZED VIEW ::::....

-- Hash Join  (cost=2271.89..2842.29 rows=15000 width=94) (actual time=46.269..85.899 rows=15000 loops=1)
--   Hash Cond: (customers.address_id = address.id)
--   ->  Hash Join  (cost=1809.39..2340.41 rows=15000 width=69) (actual time=39.404..70.922 rows=15000 loops=1)
--         Hash Cond: (home.address_id = customers.address_id)
--         ->  Hash Join  (cost=853.00..1177.77 rows=15000 width=30) (actual time=17.374..38.988 rows=15000 loops=1)
--               Hash Cond: (street.home_id = home.id)
--               ->  Hash Join  (cost=433.50..718.89 rows=15000 width=26) (actual time=8.510..21.965 rows=15000 loops=1)
--                     Hash Cond: (city.street_id = street.id)
--                     ->  Seq Scan on city  (cost=0.00..246.00 rows=15000 width=14) (actual time=0.010..4.063 rows=15000 loops=1)
--                     ->  Hash  (cost=246.00..246.00 rows=15000 width=20) (actual time=8.410..8.411 rows=15000 loops=1)
--                           Buckets: 16384  Batches: 1  Memory Usage: 910kB
--                           ->  Seq Scan on street  (cost=0.00..246.00 rows=15000 width=20) (actual time=0.006..3.273 rows=15000 loops=1)
--               ->  Hash  (cost=232.00..232.00 rows=15000 width=12) (actual time=8.788..8.788 rows=15000 loops=1)
--                     Buckets: 16384  Batches: 1  Memory Usage: 773kB
--                     ->  Seq Scan on home  (cost=0.00..232.00 rows=15000 width=12) (actual time=0.009..3.543 rows=15000 loops=1)
--         ->  Hash  (cost=768.89..768.89 rows=15000 width=39) (actual time=21.957..21.959 rows=15000 loops=1)
--               Buckets: 16384  Batches: 1  Memory Usage: 1202kB
--               ->  Hash Join  (cost=468.50..768.89 rows=15000 width=39) (actual time=6.864..16.485 rows=15000 loops=1)
--                     Hash Cond: (orders.customer_id = customers.id)
--                     ->  Seq Scan on orders  (cost=0.00..261.00 rows=15000 width=8) (actual time=0.006..1.660 rows=15000 loops=1)
--                     ->  Hash  (cost=281.00..281.00 rows=15000 width=39) (actual time=6.789..6.790 rows=15000 loops=1)
--                           Buckets: 16384  Batches: 1  Memory Usage: 1202kB
--                           ->  Seq Scan on customers  (cost=0.00..281.00 rows=15000 width=39) (actual time=0.004..2.750 rows=15000 loops=1)
--   ->  Hash  (cost=275.00..275.00 rows=15000 width=37) (actual time=6.852..6.853 rows=15000 loops=1)
--         Buckets: 16384  Batches: 1  Memory Usage: 1183kB
--         ->  Seq Scan on address  (cost=0.00..275.00 rows=15000 width=37) (actual time=0.015..2.613 rows=15000 loops=1)
-- Planning Time: 1.358 ms
-- Execution Time: 87.216 ms

-- ....::::: COST WITH MATERIALIZED VIEW :::::....

-- Seq Scan on customer_info  (cost=0.00..243.08 rows=708 width=2588) (actual time=0.007..2.021 rows=15000 loops=1)
-- Planning Time: 0.030 ms
-- Execution Time: 2.905 ms

-- create view with order and number car
CREATE VIEW order_info_with_car_number AS
    SELECT
        orders.id as order_id,
        orders.days as order_days,
        car.number as car_number
    FROM orders
    INNER JOIN car
    ON orders.car_id = car.id;

-- check this view
SELECT * FROM order_info_with_car_number;


-- create view about all TOP cars
CREATE VIEW top_cars AS
    SELECT
        car.id as car_id,
        car.number,
        car.price,
        producer_car.producer,
        model_car.model,
        car.branch_id
    FROM car
    JOIN producer_car
    ON car.id = producer_car.car_id
    JOIN model_car
    ON producer_car.id = model_car.producer_car_id
    ORDER BY car.price DESC
    LIMIT 100;

-- show this top cars
SELECT * FROM top_cars;
