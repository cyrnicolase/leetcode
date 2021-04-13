#!/usr/bin/python


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        word_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = []
        for word in words:
            item = ''
            for letter in word:
                item += word_map[ord(letter) - 97]

            result.append(item)

        return len(set(result))


words = ["gin", "zen", "gig", "msg"]
so = Solution()

print so.uniqueMorseRepresentations(words)






