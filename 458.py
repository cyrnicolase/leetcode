

# https://leetcode.com/problems/poor-pigs/description/

# 网上学习了下
# https://www.cnblogs.com/mux1/p/6275797.html

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        
        if 1 == buckets :
            return 0
        
        # 计算的维度
        demention = (minutesToTest // minutesToDie) + 1
        result = math.log(buckets, demention)
        if result == int(result):
            return int(result)
        
        return int(result) + 1
