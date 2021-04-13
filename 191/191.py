#!/usr/bin/python


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        counter = 0
        while n:
            counter += 1
            n = n & (n - 1)

        return counter

n = 4
n = 11
n = 128

so = Solution()
print so.hammingWeight(n)
