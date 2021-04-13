

# https://leetcode.com/problems/distribute-candies/description/

# -*- coding: UTF-8 -*-


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        # 去重列表,查看糖果种类数量
        candyLength = len(candies)
        kinds = list(set(candies))
        kindLength = len(kinds)
        
        if candyLength // 2 >= kindLength:
            return kindLength
        else:
            return candyLength // 2
