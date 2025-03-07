-- Script that lists all cities with their state names from the database hbtn_0d_usa
-- Each record displays: cities.id - cities.name - states.name
-- Results are sorted in ascending order by cities.id
SELECT c.id, c.name, s.name
FROM cities AS c
JOIN states AS s ON c.state_id = s.id
ORDER BY c.id ASC;
