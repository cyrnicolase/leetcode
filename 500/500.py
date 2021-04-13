
# https://leetcode.com/problems/keyboard-row/description/


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        alphabets = [
            ['Q','W','E','R','T','Y','U','I','O','P', 
             'q','w','e','r','t','y','u','i','o','p'],
            ['A','S','D','F','G','H','J','K','L',
             'a','s','d','f','g','h','j','k','l'],
            ['Z','X','C','V','B','N','M',
             'z','x','c','v','b','n','m']
        ];
        
        output = []
        for word in words:
            for alphabet in alphabets:
                flag = 1
                for letter in word:
                    if letter in alphabet:
                        continue
                    flag = 0
                    break
                
                if 1 == flag:
                    output.append(word)
        
        return output
                
            
