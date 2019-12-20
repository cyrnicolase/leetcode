class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0: 
            return [1]
        if rowIndex == 1:
            return [1, 1]

        result = (rowIndex + 1) * [1]
        last = self.getRow(rowIndex - 1)
        length = len(last)
        for i in range(length):
            if i < length -1 :
                result[i+1] = last[i] + last[i+1]

        return result

solution = Solution()
for i in range(32):
    result = solution.getRow(i)
    print(result)