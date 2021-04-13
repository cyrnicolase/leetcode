#!/usr/bin/python

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# 这个问题跟1.py 一样，只是索引变化了一下

class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        rests = {}
        for i in range(0, length):
            if nums[i] in rests:
                return [rests[nums[i]], i + 1]

            rests[target - nums[i]] = i + 1


nums = [2, 7, 11, 15]
target = 9
s = Solution()

print s.towSum(nums, target)
