#!/usr/bin/python
#-*- coding=utf-8 -*-

class Solution(object):
    '''
    逐个字符的比对,当下一个字符的长度加和超过100,则进入第二行
    '''
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        line_len = 0
        line_no = 1

        letter_map = {}
        letter_asc = 97
        for length in widths:
            letter_map[chr(letter_asc)] = length
            letter_asc += 1


        for letter in S:
            line_len += letter_map[letter]
            if 100 < line_len:
                line_no += 1
                line_len = letter_map[letter]

        return [line_no, line_len]


widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
so = Solution()
print so.numberOfLines(widths, S)

