


# https://leetcode-cn.com/problems/jewels-and-stones/description/



class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        sum = 0
        for item in J:
            sum += S.count(item)
            
        return sum
