#!/usr/bin/python
# -*- coding=utf-8 -*-

class Solution(object):
    '''
    先统计每个字符的数量
    如果存在奇数,那么只需要一个奇数,其他的都是取小于等于该数的最大偶数即可
    '''
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        letter_map = {}
        for letter in s:
            if letter_map.has_key(letter):
                letter_map[letter] += 1
                continue

            letter_map[letter] = 1

        is_odd = False
        max_len = 0
        for key, count in letter_map.items():
            if count % 2 == 0:
                max_len += count
                continue

            if not is_odd:
                max_len += count
                is_odd = True
                continue

            max_len += (count - 1)

        return max_len


input = 'abccccdd'
so = Solution()
print so.longestPalindrome(input)


        
