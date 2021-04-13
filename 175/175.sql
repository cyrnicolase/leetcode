
-- https://leetcode.com/problems/combine-two-tables/description/


SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person as p LEFT JOIN Address as a ON p.PersonId = a.PersonId ;

-- 无论有没有地址,都要显示出来, 所以应该是左表完全,右表随意. 用 LEFT JOIN



SELECT FirstName, LastName, 
    (SELECT City FROM Address WHERE PersonId = Person.PersonId) as City,
    (SELECT State FROM Address WHERE PersonId = Person.PersonId) as State 
FROM Person;

-- 用子查询的时候, 貌似不能一次返回两个字段. 用 SELECT City, State FROM Address WHERE PersonId = Person.PersonId 会出错.

