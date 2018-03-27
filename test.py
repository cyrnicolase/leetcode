#!/usr/bin/python

nums = [2, 7, 11, 15]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        rests = {}
        for i in range(0, length):
            if nums[i] in rests:
                return [rests[nums[i]], i]

            rests[target - nums[i]] = i





solution = Solution()
print solution.twoSum(nums, target)

