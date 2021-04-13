#!/usr/bin/python

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        length = len(nums)

        if 0 != nums[0]:
            return 0

        for i in range(0, length - 1):
            if nums[i] + 1 != nums[i+1]:
                return nums[i] + 1

        return nums[length - 1] + 1


nums = [3,0,1]
nums = [9,6,4,2,3,5,7,0,1]
nums = [0,1,2,3,4,5]
nums = [1]
so = Solution()
print so.missingNumber(nums)

