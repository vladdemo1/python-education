-- Task about selects with join's

-- get info about customers and orders days where days < 7
-- order firstly by days DESC and then -> car_id
SELECT
    customers.first_name,
    customers.last_name,
    orders.date,
    orders.days as order_days,
    orders.car_id
FROM customers
RIGHT JOIN orders
ON customers.id = orders.customer_id
AND orders.days < 7
WHERE customers.id IS NOT NULL
ORDER BY orders.days DESC, orders.car_id;


--select about get avg price cars and days rent
SELECT
    ROUND(AVG(car.price)) as avg_price,
    ROUND(AVG(orders.days)) as avg_days
FROM car
INNER JOIN orders
ON car.id = orders.car_id;


-- get info about rent car, price and branch id in some range
-- order in price < 500k and branch_id < 1k
EXPLAIN ANALYSE SELECT
    car.number,
    car.price,
    producer_car.producer,
    model_car.model
FROM car
JOIN producer_car
ON car.id = producer_car.car_id
JOIN model_car
ON producer_car.id = model_car.producer_car_id
AND car.price < 500000
WHERE car.branch_id < 1000
ORDER BY car.price DESC
LIMIT 50;

-- Limit  (cost=957.94..958.07 rows=50 width=62) (actual time=16.599..16.627 rows=50 loops=1)
--   ->  Sort  (cost=957.94..958.11 rows=66 width=62) (actual time=16.597..16.617 rows=50 loops=1)
--         Sort Key: car.price DESC
--         Sort Method: quicksort  Memory: 33kB
--         ->  Hash Join  (cost=653.04..955.95 rows=66 width=62) (actual time=10.249..16.550 rows=62 loops=1)
--               Hash Cond: (model_car.producer_car_id = producer_car.id)
--               ->  Seq Scan on model_car  (cost=0.00..246.00 rows=15000 width=15) (actual time=0.012..2.169 rows=15000 loops=1)
--               ->  Hash  (cost=652.21..652.21 rows=66 width=55) (actual time=10.220..10.224 rows=62 loops=1)
--                     Buckets: 1024  Batches: 1  Memory Usage: 14kB
--                     ->  Hash Join  (cost=366.82..652.21 rows=66 width=55) (actual time=3.232..10.156 rows=62 loops=1)
--                           Hash Cond: (producer_car.car_id = car.id)
--                           ->  Seq Scan on producer_car  (cost=0.00..246.00 rows=15000 width=22) (actual time=0.006..2.519 rows=15000 loops=1)
--                           ->  Hash  (cost=366.00..366.00 rows=66 width=41) (actual time=3.188..3.191 rows=62 loops=1)
--                                 Buckets: 1024  Batches: 1  Memory Usage: 13kB
--                                 ->  Seq Scan on car  (cost=0.00..366.00 rows=66 width=41) (actual time=0.010..3.152 rows=62 loops=1)
--                                       Filter: ((price < 500000) AND (branch_id < 1000))
--                                       Rows Removed by Filter: 14938
-- Planning Time: 0.714 ms
-- Execution Time: 16.683 ms

-- add indexes
CREATE INDEX car_id_idx ON car(id);
CREATE INDEX producer_car_id_idx ON producer_car(car_id);
CREATE INDEX producer_car_idx ON producer_car(id);
CREATE INDEX model_car_producer_idx ON model_car(producer_car_id);
CREATE INDEX car_price_idx ON car(price);
CREATE INDEX car_branch_id_idx ON car(branch_id);

-- get new better result

-- Limit  (cost=356.54..356.67 rows=50 width=62) (actual time=5.096..5.114 rows=50 loops=1)
--   ->  Sort  (cost=356.54..356.71 rows=66 width=62) (actual time=5.095..5.105 rows=50 loops=1)
--         Sort Key: car.price DESC
--         Sort Method: quicksort  Memory: 33kB
--         ->  Nested Loop  (cost=46.38..354.55 rows=66 width=62) (actual time=0.298..5.050 rows=62 loops=1)
--               ->  Hash Join  (cost=46.09..331.48 rows=66 width=55) (actual time=0.286..4.794 rows=62 loops=1)
--                     Hash Cond: (producer_car.car_id = car.id)
--                     ->  Seq Scan on producer_car  (cost=0.00..246.00 rows=15000 width=22) (actual time=0.007..1.747 rows=15000 loops=1)
--                     ->  Hash  (cost=45.27..45.27 rows=66 width=41) (actual time=0.266..0.268 rows=62 loops=1)
--                           Buckets: 1024  Batches: 1  Memory Usage: 13kB
--                           ->  Index Scan using car_branch_id_idx on car  (cost=0.29..45.27 rows=66 width=41) (actual time=0.016..0.245 rows=62 loops=1)
--                                 Index Cond: (branch_id < 1000)
--                                 Filter: (price < 500000)
--                                 Rows Removed by Filter: 937
--               ->  Index Scan using model_car_producer_idx on model_car  (cost=0.29..0.34 rows=1 width=15) (actual time=0.003..0.003 rows=1 loops=62)
--                     Index Cond: (producer_car_id = producer_car.id)
-- Planning Time: 0.595 ms
-- Execution Time: 5.157 ms
