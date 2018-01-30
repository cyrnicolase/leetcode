
# https://leetcode.com/problems/construct-the-rectangle/description/

import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        
        minLen = 999999999
        sqrt = int(math.sqrt(area) + 1)
        result = []
        for w in range(1, sqrt):
            if 0 != area % w:
                continue
            
            l = area / w
            if l + w < minLen:
                minLen = l + w
                result = [l , w]
                
        return result
