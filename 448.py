#!/usr/bin/python

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums.sort()
        length = len(nums)
        result = [];
        for i in range(0, length):
            if i + 1 in nums:
                continue

            result.append(i + 1)

        return result
        
so = Solution()
# 1,2,2,3,3,4,7,8
# 0,1,2,3,4,5,6,7
# 1,2,3,4,5,6,7,8
print so.findDisappearedNumbers([4,3,2,7,8,2,3,1]);
