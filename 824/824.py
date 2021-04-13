class Solution:
    def toGoatLatin(self, S):
        arr = S.split(" ")
        count = len(arr)
        result = ""
        for i in range(count):
            word = arr[i]
            if word[0] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                word += "ma"
            else:
                word = word[1:]+word[0:1]+"ma"
            word += 'a' * (i + 1)
            result += word + " "
        
        return result.strip()


S = "Each word consists of lowercase and uppercase letters only"
solution = Solution()
result = solution.toGoatLatin(S)
print(result)