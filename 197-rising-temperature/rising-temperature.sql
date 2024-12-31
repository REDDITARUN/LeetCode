# Write your MySQL query statement below
SELECT W.id 
FROM Weather W
JOIN Weather W2 
On W.recordDate = DATE_ADD(W2.recordDate, INTERVAL 1 DAY)
WHERE W.temperature > W2.temperature