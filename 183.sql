
-- https://leetcode.com/problems/customers-who-never-order/description/


SELECT Name as Customers FROM Customers 
WHERE Id NOT IN 
    (SELECT CustomerId FROM Orders); -- 117ms
