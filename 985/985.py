
class Solution:

    def sumEvenAfterQueries(self, A, queries):
        answer = []
        sum = self.sumEven(A)
        for i in range(len(A)):
            val = queries[i][0]
            index = queries[i][1]

            if 0 == A[index] % 2:
                sum -= A[index]
            A[index] += val
            if 0 == A[index] % 2:
                sum += A[index]
            answer.append(sum)

        return answer

    def sumEven(self, A):
        sum = 0
        for i in range(len(A)):
            if 0 == A[i] % 2:
                sum += A[i]
        return sum

    # def sumEvenAfterQueries(self, A, queries):
    #     answer = []
    #     sum = self.sumEven(A)
    #     for i in range(len(A)):
    #         val = queries[i][0]
    #         index = queries[i][1]

    #         # 序列原始值
    #         src = A[index]
    #         currentSum = sum
    #         if 0 == src % 2 and 0 == val % 2:
    #             currentSum += val
    #         elif 1 == src % 2 and 1 == val % 2:
    #             currentSum += val + src
    #         elif 0 == src % 2 and 1 == val % 2:
    #             currentSum -= src
    #         elif 1 == src % 2 and 0 == val % 2:
    #             currentSum += 0

    #         A[index] += val
    #         sum = currentSum
    #         answer.append(currentSum)

    #     return answer




    # def sumEvenAfterQueries(self, A, queries):
    #     answer = []
    #     for i in range(len(A)):
    #         val = queries[i][0]
    #         index = queries[i][1]
    #         A[index] += val
    #         answer.append(self.sumEven(A))

    #     return answer

    # def sumEven(self, A):
    #     sum = 0
    #     for i in range(len(A)):
    #         if 0 == A[i] % 2:
    #             sum += A[i]
    #     return sum


A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
solution = Solution()
result = solution.sumEvenAfterQueries(A, queries)
print(result)