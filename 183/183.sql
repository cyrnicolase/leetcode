
-- https://leetcode.com/problems/customers-who-never-order/description/


SELECT Name as Customers FROM Customers 
WHERE Id NOT IN 
    (SELECT CustomerId FROM Orders); -- 117ms


-- 使用Exists 确实效率要高一些

SELECT Name as Customers FROM Customers WHERE NOT EXISTS 
    (SELECT 1 FROM Orders WHERE CustomerId = Customers.Id);

