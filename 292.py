
# https://leetcode.com/problems/nim-game/description/


# -*- coding: UTF-8 -*-


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n <= 3:
            return True
        
        return False if n % 4 == 0 else True
    
# 1 W
# 2 W
# 3 W
# 4 F
# 5 W
# 6 W
# 7 W
# 8 F
# 9 W
# 10 W
# 11 W
# 12 F
# ...



