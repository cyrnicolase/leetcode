

-- https://leetcode.com/problems/second-highest-salary/description/


-- 查询最大的两个值,如果只取最后两个值,可能他们是相同的值,所以要DISTINCT
-- 然后取两个值中的最小值
-- 使用IF 函数,当最小与最大相等,说明是只有一个值. 则返回null,否则返回最小值



SELECT IF(min(tmp.Salary) = max(tmp.Salary), null, min(tmp.Salary)) as SecondHighestSalary FROM 
    (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 2) as tmp

