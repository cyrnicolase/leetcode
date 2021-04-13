
# https://leetcode.com/problems/single-number/description/

# -*- coding: UTF-8 -*-

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 首先排序
        # 然后判断相领两个值是否相等
        nums.sort()
        length = len(nums)
        
        for i in range(0, length, 2):
            if i == length - 1:
                return nums[i]           
            if i + 1 < length and nums[i] != nums[i+1]:
                return nums[i]
                
                
# 错误在语法不熟悉, 居然被坑在循环步长控制不正确....
