
# https://leetcode.com/problems/number-complement/description/


# -*- coding: UTF-8 -*-

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        mask = ~0
        while mask & num:
            mask <<= 1
        
        return ~mask & ~num
        
        
        # 偷偷学习了下,如何计算补码
        # 首先,肯定不能使用取反的操作. 因为数字32位,二进制中高位很多都是0,只是没显示出来.如果取反,则都变成1了,跟预期相差很远
        # 正解:
        # 1. 首先找到该数字的掩码.就是该数字对应位都0, 高位全都是1 那种. 比如: 0000 0101的掩码, 1111 1000 (原数字是3位,则掩码低3位都是0)
        # 2. 掩码和原码都取反,然后相& 操作,就得到原码的补码
