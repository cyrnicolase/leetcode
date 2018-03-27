#!/usr/bin/python
#-*- coding=utf-8 -*-

class Solution(object):

    smallest = 'z'

    '''
    这里应为是有序的,所以查找使用二分查找会快
    '''
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        length = len(letters)
        high = length - 1
        low = 0
        # 特殊情况,就是target为给出的letter中最大的或者更大
        if target >= letters[high]:
            return letters[0]

        # 二分查找
        while low <= high:
            mid = (high + low) // 2
            ret = self.isSmaller(letters[mid], target)

            if 1 == ret:
                low = mid + 1
            else:
                high = mid - 1

        return self.smallest



    def isSmaller(self, letter, target):
        '''
        @return 0|1 (0表示小,1表示大)
        '''

        if letter > target:
            if self.smallest > letter:
                self.smallest = letter

            return 0
        else:
            return 1




letters = ["c", "f", "j"]
target = "a"

letters = ["c", "f", "j"]
target = "c"

letters = ["c", "f", "j"]
target = "d"

letters = ["c", "f", "j"]
target = "g"

letters = ["c", "f", "j"]
target = "j"

letters = ["c", "f", "j"]
target = "k"

so = Solution()
print so.nextGreatestLetter(letters, target)

