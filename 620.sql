
-- https://leetcode.com/problems/not-boring-movies/description/

SELECT id, movie, description, rating FROM cinema WHERE id % 2 = 1 AND description NOT LIKE '%boring%' ORDER BY rating DESC;

-- 我还以为,是包含boring 的都去掉呢
