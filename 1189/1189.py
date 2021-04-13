import math

class Solution:
    def maxNumberOfBalloons(self, text):
        chars = {"b": 1,"a": 1, "l": 2,"o": 2,"n": 1}
        max = math.inf
        for (char, count) in chars.items():
            charCount = text.count(char)
            times = charCount // count
            if times < max:
                max = times
        
        return max

text = "nlaebolko"
text = "loonbalxballpoon"
solution = Solution()
result = solution.maxNumberOfBalloons(text)
print(result)