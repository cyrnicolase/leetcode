
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/description/

SELECT e.Name as Employee FROM Employee as e WHERE e.Salary > (SELECT Salary FROM Employee WHERE Id = e.ManagerId);

-- 使用了子查询, 效率稍微低了点
-- 14 / 14 test cases passed.
-- Status: Accepted
-- Runtime: 2242 ms
-- Submitted: 1 minute ago


-- 改用Join 查询

SELECT e.Name as Employee FROM Employee as e JOIN Employee as se ON e.ManagerId = se.Id WHERE e.Salary > se.Salary;

-- 14 / 14 test cases passed.
-- Status: Accepted
-- Runtime: 1763 ms
-- Submitted: 0 minutes ago

