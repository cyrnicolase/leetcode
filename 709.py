#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
DocString
'''

import string

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """

        return string.lower(str)
    

so = Solution()
print so.toLowerCase("")
