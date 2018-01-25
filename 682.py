
# https://leetcode.com/problems/baseball-game/description/


# -*- coding:UTF-8 -*-

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
	
	# 注意,判断前面值是否存在的时候,是用的 scores 列表的位移量        

        scores = []
        scoreLength = 0
        length = len(ops)
        for i in range (0, length):
            if '+' == ops[i]:
                # 如果上两个积分存在,就返回前面2个积分之和
                tmp = 0
                if scoreLength - 1 >= 0:
                    tmp += scores[scoreLength - 1]
                if scoreLength - 2 >= 0:
                    tmp += scores[scoreLength - 2]
                scores.append(tmp)
                scoreLength += 1
            elif 'D' == ops[i]:
                # 如果上一个积分存在,则dobule
                if scoreLength - 1 >= 0:
                    scores.append(scores[scoreLength - 1] * 2)
                    scoreLength += 1
            elif 'C' == ops[i]:
                # 如果存在上一个积分,去掉上一个积分
                if scoreLength - 1 >= 0 :
                    del scores[scoreLength - 1]  # scores.pop()
                    scoreLength -= 1
            else:
                scores.append(int(ops[i]))   # 数字,直接进入表, 这里需要注意,字符串跟数字之间的转换
                scoreLength += 1
            
        # 求和
        sum = 0
        for score in scores:
            sum += score
        
        return sum
        
