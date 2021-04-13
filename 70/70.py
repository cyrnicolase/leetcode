

# https://leetcode.com/problems/climbing-stairs/description/

# 一开始使用递归的方式,出现超时错误
# 然后看了下讨论,原来递归的复杂度太高...

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        if 0 == n:
            return 0
        if 1 == n:
            return 1
        if 2 == n:
            return 2
        
        first = 1
        second = 2
        result = 0
        
        for i in range (3, n+1):
            result = first + second
            tmp = second
            first = second
            second = result
            
        return result
