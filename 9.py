#!/usr/bin/python

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        strs = str(x)
        length = len(strs)
        half = length // 2
        i = 0
        while i <= half:
            if strs[i] != strs[length - i - 1]:
                return False

            i += 1

        return True

x = 10
so = Solution()
print so.isPalindrome(x)
