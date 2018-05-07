#!/usr/bin/python


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count_values = {}
        for num in nums:
            if count_values.has_key(num):
                count_values[num] += 1
            else:
                count_values[num] = 1

        max_count = 0
        result = None
        for num, count in count_values.items():
            if max_count < count:
                max_count = count
                result = num

        return result
        

nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
so = Solution()
print so.majorityElement(nums)
