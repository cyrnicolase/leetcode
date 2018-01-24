
-- https://leetcode.com/problems/duplicate-emails/description/

SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1;
