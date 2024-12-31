# Write your MySQL query statement below
SELECT prod.product_name, sal.year, sal.price 
FROM Sales sal
LEFT JOIN Product prod ON sal.product_id = prod.product_id