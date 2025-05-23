-- Write your PostgreSQL query statement below
SELECT e1.employee_id AS employee_id, MAX(e1.name) as name, 
COUNT(e2.reports_to) AS reports_count,
ROUND(AVG(e2.age)) AS average_age
FROM Employees e1
JOIN Employees e2 ON 
e1.employee_id = e2.reports_to
GROUP BY e1.employee_id
ORDER BY employee_id;