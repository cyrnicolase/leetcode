
# https://leetcode.com/problems/self-dividing-numbers/description/

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        while left <= right:
            number = left
            flag = 1
            while number > 0:
                latestNumber = number % 10
                
                if 0 == latestNumber or 0 != left % latestNumber:
                    flag = 0
                    break
                number = number // 10
            
            if flag:
                result.append(left)
            left += 1

        return result
