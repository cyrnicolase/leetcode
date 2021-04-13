from itertools import chain

class Solution:
    # 判断点位数量是否一致，不一致，则直接返回不可构造，返回原始结构
    def matrixReshape(self, nums, r, c):
        if not nums:
            return nums

        if not self.isUnitMatch(nums, r, c):
            return nums

        line = list(chain.from_iterable(nums))
        k, result = 0, [0] * r
        for i in range(r):
            unit = []
            for j in range(c):
                unit.append(line[k])
                k += 1
            result[i] = unit
        return result
        
    # 判断两个矩阵的点是否相同
    def isUnitMatch(self, nums, r, c):
        origin = len(nums) * len(nums[0])
        return origin == r * c


nums = [[1,2],[3,4]]
r = 4
c = 1
solution = Solution()
result = solution.matrixReshape(nums, r, c)
print(result)