
# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# -*- coding: UTF-8 -*-
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # 首先将所有的字符唯一化,减少查询次数
        # 考虑到题目需要查找第一个出现的,所以要保持原来的顺序
        # 字符串从做向右查找,从右向左查找是同一个值的,且不是-1 ,那么就是没有重复出现的
        ss = list(s)
        letters = list(set(ss))
        letters.sort(key = ss.index)  # 按照原始字符串排序
        
        for letter in letters:
            index = s.find(letter)
            if index == s.rfind(letter) and -1 != index:
                return index
        
        return -1
        
