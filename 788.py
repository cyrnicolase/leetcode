#!/usr/bin/python
#-*- coding=utf-8 -*-


class Solution(object):
    
    num_map = {
        '0': '0',
        '1': '1',
        '2': '5',
        '3': None,
        '4': None,
        '5': '2',
        '6': '9',
        '7': None,
        '8': '8',
        '9': '6'
    }

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        result = []
        for i in range(1, N+1):
            is_good_num = True
            str_i = str(i)

            new_num = ''
            for digit in str_i:
                r_digit = self.num_map[digit]
                if None == r_digit:
                    is_good_num = False
                    break;

                new_num += r_digit
            
            if is_good_num and int(new_num) != i:
                result.append(i)

        return len(result)


n = 10
so = Solution()
print so.rotatedDigits(n)
