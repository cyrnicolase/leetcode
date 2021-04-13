#!/usr/bin/python

# https://leetcode.com/problems/two-sum/description/

# 学习了，这种情况，是2个数的和，那么就将每个数的差值存储下来。
# 判断后面的数是否在差值结果集中，存在这返回。O(n)

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

