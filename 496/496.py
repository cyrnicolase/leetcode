
# https://leetcode.com/problems/next-greater-element-i/description/


# -*- coding: UTF-8 -*-

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []
        length = len(nums)
        for f in findNums:
            index = nums.index(f)
            flag = 1
            for index in range(index, length):
                if f < nums[index]:
                    result.append(nums[index])
                    flag = 0
                    break;
            
            if flag:
                result.append(-1)
                
        return result
