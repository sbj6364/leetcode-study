# Write your MySQL query statement below
SELECT name, bonus
FROM Employee e LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus IS null or b.bonus < 1000