
# https//leetcode.com/problems/find-the-difference/description/

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)
        t = list(t)
    
        s.sort()
        t.sort()
        
        length = len(t)
        for i in range(0, length):
            if i < length - 1 and s[i] != t[i]:
                return t[i]
            
            if i == length - 1:
                return t[i]
            
        
        
        
