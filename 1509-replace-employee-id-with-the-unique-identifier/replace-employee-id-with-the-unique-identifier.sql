-- Write your PostgreSQL query statement below

SELECT eu.unique_id, e.name FROM Employees e 
LEFT JOIN Employeeuni eu ON eu.id = e.id;
