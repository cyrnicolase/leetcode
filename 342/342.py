#!/usr/bin/python


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if 1 == num:
            return True
        
        i = 2
        base_num = 1
        while i < 32:
            base_num <<= 2
            if num == base_num:
                return True

            if num < base_num:
                return False
            i += 2

        return False


num = 0
num = 16
num = 5
num = 1
num = 3
so = Solution()
print so.isPowerOfFour(num)
