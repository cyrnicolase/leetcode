
class Solution:

    def minimumAbsDifference(self, arr):
        arr.sort()
        arrMap = {}
        count = len(arr)
        min = 99999
        for i in range(count - 1):
            diff = arr[i+1] - arr[i]
            min = diff if diff < min else min
            if diff in arrMap:
                arrMap[diff].append([arr[i], arr[i+1]])
            else:
                arrMap[diff] = [[arr[i], arr[i+1]]]

        return arrMap[min]


arr = [4,2,1,3]
arr = [1,3,6,10,15]
arr = [3,8,-10,23,19,-4,-14,27]
solution = Solution()
result = solution.minimumAbsDifference(arr)
print(result)
