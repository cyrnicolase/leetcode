# -*- coding:utf-8 -*-

class Solution:
    def countCharacters(self, words, chars):
        count = 0
        for word in words:
            flag = 1
            for c in word:
                if word.count(c) > chars.count(c):
                    flag = 0
                    break
            if 1 == flag:
                count += len(word)

        return count

# class Solution:
#     def countCharacters(self, words, chars):
#         mapChars = self.countChars(chars)
#         count = 0
#         for word in words:
#             temp = mapChars.copy()
#             if self.compareWord(word, temp):
#                 count += len(word)
#         return count

#     # 统计字母表各个字符的数量返回一个map
#     def countChars(self, chars):
#         result = {}
#         for c in chars:
#             if c in result:
#                 result[c] += 1
#             else:
#                 result[c] = 1

#         return result

#     # 比对单词，通过每个字母的数量进行自减
#     def compareWord(self, word, mapChars):
#         for c in word :
#             if c not in mapChars:
#                 return False
            
#             mapChars[c] -= 1
#             if 0 > mapChars[c]:
#                 return False
        
#         return True


words = ["cat","bt","hat","tree"]
chars = "atach"
solution = Solution()
print(solution.countCharacters(words, chars))