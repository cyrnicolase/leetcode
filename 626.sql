

-- https://leetcode.com/problems/exchange-seats/description/



-- 以前了解过 CASE WHEN 做IF 判断
-- 但是还没有用到过这么相对比较复杂的判断过程

SELECT 
    CASE  
        WHEN id % 2 = 0 THEN
            id - 1
        ELSE
            CASE 
                WHEN id < (SELECT COUNT(1) FROM seat) THEN
                    id + 1 
                ELSE
                    id
            END
    END as id,
    student
    
FROM seat 
ORDER BY id;
