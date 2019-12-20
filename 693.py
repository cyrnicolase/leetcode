class Solution:

    def hasAlternatingBits(self, n):
        x = n % 2
        while n > 0:
            n = n >> 1
            if x == n % 2:
                return False
            x = n % 2

        return True


n = 3
solution = Solution()
result = solution.hasAlternatingBits(n)
print(result)