
-- https://leetcode.com/problems/classes-more-than-5-students/description/


SELECT class FROM courses GROUP BY class HAVING COUNT(DISTINCT student) >= 5;

-- 这里遇到一个坑, 是说不能包含重复的学生, 开始没注意,直接用 HAVING COUNT(class) 就Fail 了. GROUP BY 的字段必须在查询结果中.
-- 但是 HAVING 中的字段好像就不用必须出现在查询结果中
