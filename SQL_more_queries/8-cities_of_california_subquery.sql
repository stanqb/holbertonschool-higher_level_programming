-- Script that lists all the cities of California from the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
-- Uses a subquery to find cities where state_id matches California's id
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
