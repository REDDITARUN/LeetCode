-- Write your PostgreSQL query statement below

SELECT s.year, s.price, p.product_name 
FROM Product p INNER JOIN Sales s
ON p.product_id = s.product_id;
