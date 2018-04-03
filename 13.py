#!/usr/bin/python
# -*- coding=utf-8 -*-

class Solution(object):

    # roman_map = [
    #     ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    #     ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    #     ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    #     ['', 'M', 'MM', 'MMM']
    # ]

    # def __init__(self):
    #     nums = {}
    #     for i in range(0, 3999):
    #         item = ''
    #         item += str(self.roman_map[3][i / 1000 % 10])
    #         item += str(self.roman_map[2][i / 100 % 10])
    #         item += str(self.roman_map[1][i / 10 % 10])
    #         item += str(self.roman_map[0][i % 10])
    #         nums[item] = i

    #     self.nums = nums


    # def romanToInt(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """


    #     return self.nums[s]

    #######################################################################

    roman_map = {
        'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
        'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90,
        'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900,
        'M': 1000, 'MM': 2000, 'MMM': 3000
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        使用贪婪匹配的方式,一直找到最大的匹配串,并作为值返回
        """

        unit = ''
        unit_sum = 0
        total = 0
        for letter in s:
            unit += letter
            if self.roman_map.has_key(unit):
                unit_sum = self.roman_map[unit]
            else:
                unit = letter
                total += unit_sum
                unit_sum = self.roman_map[unit]

        return total + unit_sum




roman = 'MCMXC'
roman = 'MCMLXXVI'
roman = 'III'
roman = 'IV'
roman = 'DCXXI'
roman = 'MDCCCLXXXVIII'
so = Solution()
print so.romanToInt(roman)

        
