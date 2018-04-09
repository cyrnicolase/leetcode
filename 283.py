#!/usr/bin/python

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        new_length = length = len(nums)
        i = 0
        while i < length:
            if 0 == nums[i]:
                j = i
                while j < length - 1:
                    nums[j] = nums[j+1]
                    j += 1

                nums[length - 1] = 0
                length -= 1
            else:
                i += 1
        
        return nums


nums = [0, 1, 0, 3, 12]
so = Solution()
print so.moveZeroes(nums)
