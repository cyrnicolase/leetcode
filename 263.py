
# https://leetcode.com/problems/ugly-number/description/


#!/usr/bin/python
# -*- coding:UTF-8 -*-

import math

# 这个判断效率很低.其中一个优化,可以是将素数存储起来.不用重复计算

# 学习了别人的方法, 排除正确的,剩下的都是错误的.
# 将输入的数值不断的变小,计算量就变小了, while 0 == n % 2: n /= 2; while 0 == n % 3: n /= 3; while 0 == n % 5: n /= 5;
# 这样, 这写结果都是True, 不然都是 False

# 合数肯定能被一批素数整除, 不是2,3,5 就是其他的,只要有其他的,就是 False

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if 1 == num:
            return True
        
        if num <= 0:
            return False
        
        return self.fetchFactorsOfNum(num)
        
        
    # 获取该数字的所有因子
    def fetchFactorsOfNum(self, num):
        sqrt = math.sqrt(num)
        sqrt = int(sqrt) + 1

        for i in range(1, sqrt):
            if num % i == 0:
                item1 = i
                item2 = num / i
                
                if self.isPrimeNumber(item1) and i not in [2, 3, 5]:
                    return False
                
                if self.isPrimeNumber(item2) and item2 not in [2, 3, 5]:
                    return False
                
        return True
                
                

    # 判断数字是否为素数
    def isPrimeNumber(self, num):
        sqrt = math.sqrt(num)
        sqrt = int(sqrt) + 1
        
        if 1 == num:
            return False
        elif 2 == num:
            return True
        elif 3 == num:
            return True
        
        for i in range(2, sqrt):
            if num % i == 0:
                return False

        return True


