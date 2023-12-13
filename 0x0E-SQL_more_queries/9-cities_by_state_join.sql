-- lists all cities contained in the database
USE hbtn_0d_usa;
SELECT cities.id AS city_id, cities.name AS city_name, states.name AS state_name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
