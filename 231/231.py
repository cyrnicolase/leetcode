
# https://leetcode.com/problems/power-of-two/description/


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        items = self.powerOfTwo()
        if n in items:
            return True
    
        return False
        
    
    def powerOfTwo(self):
        result = []
        for i in range(0, 33):
            result.append(math.pow(2, i))
            
        return result
