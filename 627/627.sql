
-- https://leetcode.com/problems/swap-salary/description/


UPDATE salary SET sex = IF('m' = sex, 'f', 'm');

-- IF(exp1, exp2, exp3); 如果 exp1 为真, 返回 exp2, 否则返回 exp3

UPDATE salary 
SET sex = CASE sex WHEN 'f' THEN 'm'
                   ELSE 'f' END;
                   
-- CASE WHEN . 
--
-- CASE number WHEN 1 THEN 'one'
--             WHEN 2 THEN 'two'
--             WHEN 3 THEN 'three'
--             ELSE 'big number'
-- END

