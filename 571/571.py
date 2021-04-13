
# https://leetcode.com/problems/array-partition-i/description/

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # sort, and fetch n % 1 == 0  
        
        nums.sort()
        length = len(nums)
        sum = 0
        for i in range(0, length):
            if i % 2 == 0:
                sum += nums[i]
                
        return sum
