# https://leetcode.com/problems/judge-route-circle/description/

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        x = 0
        y = 0
        for i in range (0, len(moves)):
            if 'U' == moves[i] :
                x += 1
            elif 'D' == moves[i]:
                x -= 1
            elif 'L' == moves[i]:
                y -= 1
            elif 'R' == moves[i]:
                y += 1
            
        return True if 0 == x and 0 == y else False
