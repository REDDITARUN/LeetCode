-- Write your PostgreSQL query statement below
SELECT v.customer_id,  count(v.customer_id) as count_no_trans
from visits v LEFT JOIN Transactions t 
ON v.visit_id = t.visit_id
WHERE t.visit_id is null
GROUP BY v.customer_id