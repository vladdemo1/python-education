-- Create first table with bananas
CREATE TEMPORARY TABLE bananas(
  id INTEGER,
  type_banana VARCHAR(100),
  count INT
);
-- insert some values to this table
INSERT INTO bananas
SELECT i, md5(random()::text), i
FROM generate_series(1, 1000000) AS i;
-- create next table
CREATE TEMPORARY TABLE gorillas(
    id INTEGER,
    gorilla_name VARCHAR(100)
);
-- insert some data
INSERT INTO gorillas
SELECT i, md5(random()::text)
FROM generate_series(500000, 1500000) AS i;
-- get gorillas bananas
EXPLAIN SELECT gorilla_name, bananas.count AS count_bananas
FROM gorillas
LEFT JOIN bananas
ON gorillas.id = bananas.count
WHERE bananas.count IS NOT NULL
ORDER BY bananas.count DESC
LIMIT 100;
-- First start this and have big cost all Limit
--
-- Limit  (cost=135015.15..135016.65 rows=100 width=222)
--   ->  Merge Join  (cost=135015.15..6089108.66 rows=396801075 width=222)
--         Merge Cond: (gorillas.id = bananas.count)
--         ->  Sort  (cost=91553.86..92220.58 rows=266688 width=222)
--               Sort Key: gorillas.id DESC
--               ->  Seq Scan on gorillas  (cost=0.00..11000.88 rows=266688 width=222)
--         ->  Materialize  (cost=43461.29..44949.17 rows=297577 width=4)
--               ->  Sort  (cost=43461.29..44205.23 rows=297577 width=4)
--                     Sort Key: bananas.count DESC
--                     ->  Seq Scan on bananas  (cost=0.00..12336.72 rows=297577 width=4)
--                           Filter: (count IS NOT NULL)
-- JIT:
--   Functions: 14
-- "  Options: Inlining false, Optimization false, Expressions true, Deforming true"


-- Add indexes
CREATE INDEX ON bananas(count);
CREATE INDEX ON gorillas(id);
-- start again block in lines 21-27 and have optimize cost for Limit in this situation
--
-- Limit  (cost=0.85..2.35 rows=100 width=222)
--   ->  Merge Join  (cost=0.85..74752603.49 rows=4975004975 width=222)
--         Merge Cond: (bananas.count = gorillas.id)
--         ->  Index Only Scan Backward using bananas_count_idx on bananas  (cost=0.42..65724.93 rows=995000 width=4)
--               Index Cond: (count IS NOT NULL)
--         ->  Materialize  (cost=0.42..61816.44 rows=1000001 width=222)
--               ->  Index Scan Backward using gorillas_id_idx on gorillas  (cost=0.42..59316.44 rows=1000001 width=222)

-- Second work with indexes + memory size
-- create first table with car
CREATE TEMPORARY TABLE car(
    id INT,
    count INT,
    color VARCHAR(100)
);
-- create table with market
CREATE TEMPORARY TABLE market(
    id INT,
    contains_count_car INT
);
-- fulling this tables
-- fulling cars
INSERT INTO car
SELECT i, i*2, md5(random()::text)
FROM generate_series(0, 1000000) AS i;
-- fulling markets
INSERT INTO market
SELECT i, i
FROM generate_series(0, 1000000) AS i;
-- check this tables
EXPLAIN ANALYSE SELECT car.id, car.count, market.id
FROM car
INNER JOIN market
ON car.count = market.contains_count_car
ORDER BY car.count DESC
LIMIT 500;
-- default explain
--
-- Limit  (cost=171392.20..171399.71 rows=500 width=12) (actual time=1171.664..1172.495 rows=500 loops=1)
--   ->  Merge Join  (cost=171392.20..22606909.21 rows=1495434768 width=12) (actual time=1162.539..1163.294 rows=500 loops=1)
--         Merge Cond: (car.count = market.contains_count_car)
--         ->  Sort  (cost=43629.02..44376.70 rows=299072 width=8) (actual time=579.140..653.876 rows=500500 loops=1)
--               Sort Key: car.count DESC
--               Sort Method: external merge  Disk: 17696kB
--               ->  Seq Scan on car  (cost=0.00..12336.72 rows=299072 width=8) (actual time=0.052..241.752 rows=1000001 loops=1)
--         ->  Materialize  (cost=127763.19..132763.44 rows=1000050 width=8) (actual time=451.302..451.644 rows=999 loops=1)
--               ->  Sort  (cost=127763.19..130263.31 rows=1000050 width=8) (actual time=451.256..451.412 rows=999 loops=1)
--                     Sort Key: market.contains_count_car DESC
--                     Sort Method: external merge  Disk: 17696kB
--                     ->  Seq Scan on market  (cost=0.00..14425.50 rows=1000050 width=8) (actual time=0.041..144.952 rows=1000001 loops=1)
-- Planning Time: 0.073 ms
-- JIT:
--   Functions: 10
-- "  Options: Inlining false, Optimization false, Expressions true, Deforming true"
-- "  Timing: Generation 0.799 ms, Inlining 0.000 ms, Optimization 0.301 ms, Emission 8.674 ms, Total 9.774 ms"
-- Execution Time: 1179.592 ms

-- and add indexes
CREATE INDEX ON car(count);
CREATE INDEX ON market(contains_count_car);
-- Start again selects on lines 81 - 86
--
-- Limit  (cost=0.85..8.36 rows=500 width=12) (actual time=149.622..150.487 rows=500 loops=1)
--   ->  Merge Join  (cost=0.85..75109694.88 rows=5000010000 width=12) (actual time=149.620..150.428 rows=500 loops=1)
--         Merge Cond: (car.count = market.contains_count_car)
--         ->  Index Scan Backward using car_count_idx on car  (cost=0.42..63364.44 rows=1000001 width=8) (actual time=0.046..100.976 rows=500500 loops=1)
--         ->  Materialize  (cost=0.42..46180.44 rows=1000001 width=8) (actual time=0.034..0.431 rows=999 loops=1)
--               ->  Index Scan Backward using market_contains_count_car_idx on market  (cost=0.42..43680.44 rows=1000001 width=8) (actual time=0.029..0.229 rows=999 loops=1)
-- Planning Time: 0.653 ms
-- Execution Time: 150.561 ms
--
-- Add small size memory
SET work_mem TO '4MB';
--
-- Delete Indexes for check next result
DROP INDEX market_contains_count_car_idx;
DROP INDEX car_count_idx;
-- Start again lines 81-86
--
-- Limit  (cost=260435.92..260443.42 rows=500 width=12) (actual time=1124.226..1125.138 rows=500 loops=1)
--   ->  Merge Join  (cost=260435.92..75268085.93 rows=5000010000 width=12) (actual time=1115.380..1116.229 rows=500 loops=1)
--         Merge Cond: (car.count = market.contains_count_car)
--         ->  Sort  (cost=132678.46..135178.46 rows=1000001 width=8) (actual time=568.115..646.095 rows=500500 loops=1)
--               Sort Key: car.count DESC
--               Sort Method: external merge  Disk: 17696kB
--               ->  Seq Scan on car  (cost=0.00..19346.01 rows=1000001 width=8) (actual time=0.030..204.560 rows=1000001 loops=1)
--         ->  Materialize  (cost=127757.46..132757.46 rows=1000001 width=8) (actual time=408.976..409.376 rows=999 loops=1)
--               ->  Sort  (cost=127757.46..130257.46 rows=1000001 width=8) (actual time=408.971..409.148 rows=999 loops=1)
--                     Sort Key: market.contains_count_car DESC
--                     Sort Method: external merge  Disk: 17696kB
--                     ->  Seq Scan on market  (cost=0.00..14425.01 rows=1000001 width=8) (actual time=0.020..107.869 rows=1000001 loops=1)
-- Planning Time: 0.108 ms
-- JIT:
--   Functions: 10
-- "  Options: Inlining false, Optimization false, Expressions true, Deforming true"
-- "  Timing: Generation 1.403 ms, Inlining 0.000 ms, Optimization 0.477 ms, Emission 8.177 ms, Total 10.057 ms"
-- Execution Time: 1132.971 ms
--
-- Again create indexes + small size memory
CREATE INDEX ON car(count);
CREATE INDEX ON market(contains_count_car);
-- Check next result -> start lines 81-86
--
-- Limit  (cost=0.85..8.36 rows=500 width=12) (actual time=189.754..191.029 rows=500 loops=1)
--   ->  Merge Join  (cost=0.85..75109694.88 rows=5000010000 width=12) (actual time=189.753..190.938 rows=500 loops=1)
--         Merge Cond: (car.count = market.contains_count_car)
--         ->  Index Scan Backward using car_count_idx on car  (cost=0.42..63364.44 rows=1000001 width=8) (actual time=0.054..130.686 rows=500500 loops=1)
--         ->  Materialize  (cost=0.42..46180.44 rows=1000001 width=8) (actual time=0.029..0.603 rows=999 loops=1)
--               ->  Index Scan Backward using market_contains_count_car_idx on market  (cost=0.42..43680.44 rows=1000001 width=8) (actual time=0.027..0.332 rows=999 loops=1)
-- Planning Time: 0.519 ms
-- Execution Time: 191.094 ms
--

-- And now set memory size 200Mb and check new result
SET work_mem TO '200MB';
-- Start lines 81-86
--
-- Limit  (cost=0.85..8.36 rows=500 width=12) (actual time=152.166..152.989 rows=500 loops=1)
--   ->  Merge Join  (cost=0.85..75109694.88 rows=5000010000 width=12) (actual time=152.164..152.914 rows=500 loops=1)
--         Merge Cond: (car.count = market.contains_count_car)
--         ->  Index Scan Backward using car_count_idx on car  (cost=0.42..63364.44 rows=1000001 width=8) (actual time=0.045..103.259 rows=500500 loops=1)
--         ->  Materialize  (cost=0.42..46180.44 rows=1000001 width=8) (actual time=0.018..0.384 rows=999 loops=1)
--               ->  Index Scan Backward using market_contains_count_car_idx on market  (cost=0.42..43680.44 rows=1000001 width=8) (actual time=0.015..0.191 rows=999 loops=1)
-- Planning Time: 0.160 ms
-- Execution Time: 153.049 ms

-- 3d example
-- create table with tallest people
CREATE TEMPORARY TABLE people(
    id INT,
    name VARCHAR(100),
    height INT
);
-- insert to people some data
INSERT INTO people
SELECT i, md5(random()::text), i
FROM generate_series(0, 1000000) AS i;
-- create aliens
CREATE TEMPORARY TABLE alien(
  id INT,
  height_alien INT
);
-- fulling aliens
INSERT INTO alien
SELECT i/5, i
FROM generate_series(0, 5000000, 5) AS i;
-- create somethings locations for live people and aliens
CREATE TEMPORARY TABLE home(
    id INT,
    location VARCHAR(100)
);
-- add two locations
INSERT INTO home VALUES (0, 'Mars');
INSERT INTO home VALUES (1, 'Earth');
-- create default view
CREATE VIEW big_aliens AS
SELECT people.id, people.height, alien.height_alien
FROM people
INNER JOIN alien
ON people.height = alien.height_alien;
-- get all entities where height ending on ..0
EXPLAIN ANALYSE SELECT
    height AS height_human,
    height_alien,
    home.location AS real_home
FROM big_aliens
INNER JOIN home
ON height_alien % 10 = home.id
ORDER BY height_alien DESC
LIMIT 1000;
--
-- standard operation and result after this select
--
-- Limit  (cost=171392.20..174901.58 rows=1000 width=226) (actual time=1443.956..1450.278 rows=1000 loops=1)
--   ->  Nested Loop  (cost=171392.20..8397041624.01 rows=2392695629 width=226) (actual time=1431.603..1437.791 rows=1000 loops=1)
--         Join Filter: ((alien.height_alien % 10) = home.id)
--         Rows Removed by Join Filter: 2997
--         ->  Merge Join  (cost=171392.20..22606909.21 rows=1495434768 width=8) (actual time=1431.573..1436.225 rows=1999 loops=1)
--               Merge Cond: (people.height = alien.height_alien)
--               ->  Sort  (cost=43629.02..44376.70 rows=299072 width=4) (actual time=533.903..535.717 rows=9991 loops=1)
--                     Sort Key: people.height DESC
--                     Sort Method: external merge  Disk: 13800kB
--                     ->  Seq Scan on people  (cost=0.00..12336.72 rows=299072 width=4) (actual time=0.028..206.058 rows=1000001 loops=1)
--               ->  Materialize  (cost=127763.19..132763.44 rows=1000050 width=4) (actual time=492.321..782.552 rows=801999 loops=1)
--                     ->  Sort  (cost=127763.19..130263.31 rows=1000050 width=4) (actual time=492.315..625.677 rows=801999 loops=1)
--                           Sort Key: alien.height_alien DESC
--                           Sort Method: external merge  Disk: 13800kB
--                           ->  Seq Scan on alien  (cost=0.00..14425.50 rows=1000050 width=4) (actual time=0.020..173.919 rows=1000001 loops=1)
--         ->  Materialize  (cost=0.00..14.80 rows=320 width=222) (actual time=0.000..0.000 rows=2 loops=1999)
--               ->  Seq Scan on home  (cost=0.00..13.20 rows=320 width=222) (actual time=0.019..0.021 rows=2 loops=1)
-- Planning Time: 0.178 ms
-- JIT:
--   Functions: 18
-- "  Options: Inlining false, Optimization false, Expressions true, Deforming true"
-- "  Timing: Generation 1.932 ms, Inlining 0.000 ms, Optimization 0.519 ms, Emission 11.537 ms, Total 13.988 ms"
-- Execution Time: 1457.618 ms
--

-- then add next indexes
CREATE INDEX ON alien(height_alien);
CREATE INDEX ON people(height);
CREATE INDEX ON home(id);
--
-- Start again this Select on lines 220-228
--
-- Limit  (cost=0.85..18.69 rows=1000 width=226) (actual time=823.619..832.673 rows=1000 loops=1)
--   ->  Merge Join  (cost=0.85..892071.69 rows=50000100 width=226) (actual time=823.617..832.550 rows=1000 loops=1)
--         Merge Cond: (alien.height_alien = people.height)
--         ->  Nested Loop  (cost=0.42..78681.50 rows=10000 width=222) (actual time=0.070..797.536 rows=401000 loops=1)
--               Join Filter: ((alien.height_alien % 10) = home.id)
--               Rows Removed by Join Filter: 1202997
--               ->  Index Only Scan Backward using alien_height_alien_idx on alien  (cost=0.42..43680.44 rows=1000001 width=4) (actual time=0.050..214.459 rows=801999 loops=1)
--                     Heap Fetches: 801999
--               ->  Materialize  (cost=0.00..1.03 rows=2 width=222) (actual time=0.000..0.000 rows=2 loops=801999)
--                     ->  Seq Scan on home  (cost=0.00..1.02 rows=2 width=222) (actual time=0.010..0.012 rows=2 loops=1)
--         ->  Materialize  (cost=0.42..65864.44 rows=1000001 width=4) (actual time=0.025..5.353 rows=9991 loops=1)
--               ->  Index Only Scan Backward using people_height_idx on people  (cost=0.42..63364.44 rows=1000001 width=4) (actual time=0.023..2.841 rows=9991 loops=1)
--                     Heap Fetches: 9991
-- Planning Time: 0.623 ms
-- Execution Time: 832.795 ms
