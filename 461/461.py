# https://leetcode.com/problems/hamming-distance/description/

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        n = x ^ y
        while n:
            count += 1
            n &= (n - 1)
            
        return count
