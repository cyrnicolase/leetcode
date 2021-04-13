class Solution:
    def lastStoneWeight(self, stones):
        while 1 < len(stones):
            stones.sort()
            max1 = stones.pop()
            max2 = stones.pop()
            stones.append(max1 - max2)
        return stones.pop()

arr = [2,7,4,1,8,1]
# arr =[7,6,7,6,9]
solution = Solution()
result = solution.lastStoneWeight(arr)
print(result)