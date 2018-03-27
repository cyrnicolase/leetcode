#!/usr/bin/python

import math

class Solution(object):
    cycle = []
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if 1 == n:
            return True
        
        while True:

            n = self.sumSelf(n)
            if n in self.cycle:
                return False

            if 1 == n:
                return True

            self.cycle.append(n)

            

    def sumSelf(self, n):
        print n
        result = 0
        while n > 0:
            num = n % 10
            n /= 10
            result += math.pow(num, 2)

        result = int(result)
        return result

so = Solution()
print so.isHappy(15)
