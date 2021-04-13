



class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # return s[::-1] 

        # 下面这个方案在Leetcode 超时,但是对比上面一个方案,速度还快一些
        length = len(s)
        output = ''
        while length > 0:
            length -= 1
            output += s[length]
            
        return output
