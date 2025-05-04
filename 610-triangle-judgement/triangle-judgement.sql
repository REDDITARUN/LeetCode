-- Write your PostgreSQL query statement below
SELECT x, y, z, 
CASE WHEN  x + y > z and y + z > x AND x + z > y THEN 'Yes' ELSE 'No' END AS triangle
FROM Triangle;