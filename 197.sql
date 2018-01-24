

-- https://leetcode.com/problems/rising-temperature/description/


SELECT w1.Id FROM Weather as w1 JOIN Weather as w2 ON date_sub(w1.Date, INTERVAL 1 DAY) = w2.Date 
WHERE w1.Temperature > w2.Temperature; -- 103 ms


-- 这里用到一个日期函数 DATE_SUB();    DATE_ADD();  第二个参数一定要有 INTERVAL 关键字
