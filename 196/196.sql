
-- https://leetcode.com/problems/delete-duplicate-emails/description/


-- 查询出所有重复邮件的记录
-- SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1

-- 按照邮件分组,查询出每组最小Id
-- SELECT MIN(Id) FROM Person GROUP BY Email HAVING COUNT(Email) > 1


DELETE FROM Person 
WHERE Email In (SELECT p1.Email FROM (select * from Person) as p1 GROUP BY p1.Email HAVING COUNT(p1.Email) > 1) 
AND Id NOT IN (SELECT MIN(p2.Id) FROM (select * from Person) as p2 GROUP BY p2.Email HAVING COUNT(p2.Email) > 1) 


-- 这里有个很有意思的问题, 在子查询里面,使用了临时表. 先将原始表的数据查询到临时表,再从临时表中查询结果出来判断
-- 这样做的原因是,规避 You can't specify target table 'Person' for update in FROM clause  这个问题


-- http://blog.csdn.net/anya/article/details/6407280/   从这里了解到 min(Id) 查询
-- http://www.cnblogs.com/chy1000/archive/2010/03/02/1676282.html  从这里找到解决子查询的问题



