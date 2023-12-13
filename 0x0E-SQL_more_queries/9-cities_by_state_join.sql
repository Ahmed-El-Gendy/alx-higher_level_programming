-- lists all cities contained in the database
SELECT cities.id AS id, cities.name AS name, states.name AS name 
FROM cities cities
INNER JOIN states states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
