#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
DocString
'''

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        length = len(A)
        for i in range(0, length):
            row = A[i]
            reverseRow = row[::-1]

