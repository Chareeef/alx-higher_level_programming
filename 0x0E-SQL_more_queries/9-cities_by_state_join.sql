-- list all cities and states
SELECT c.id, c.name, s.name
FROM cities c
JOIN states s
ON s.id = c.state_id
ORDER BY c.id;
