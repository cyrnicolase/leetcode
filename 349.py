#!/usr/bin/python

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        result = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    result.append(num1)
                    nums2.remove(num2)
                    break

        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
so = Solution()
print so.intersection(nums1, nums2)
        
