
# https://leetcode.com/problems/fizz-buzz/description/



class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range (1, n+1):
            fizz = ''
            buzz = ''
            
            if 0 == i % 3:
                fizz = 'Fizz'
            if 0 == i % 5:
                buzz = 'Buzz'
                
            item = fizz + buzz
            if item:
                result.append(item)
            else:
                result.append(str(i))
                
        return result
