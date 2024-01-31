# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees E LEFT JOIN EmployeeUNI EU on E.id = EU.id