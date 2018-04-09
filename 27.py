#!/usr/bin/python

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        length = len(nums)
        for i in range(0, length):
            while i < length and nums[i] == val:
                nums[i] = nums[length - 1]
                nums.pop()
                length -= 1

        return len(nums)
       

nums = [3, 2, 2, 3]
val = 3
so = Solution()
print so.removeElement(nums, val)
