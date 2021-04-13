# https://leetcode.com/problems/find-anagram-mappings/description/

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        result = []
        for ia in range(0, len(A)):
            for ib in range(0, len(B)):
                if A[ia] == B[ib]:
                    result.append(ib)
                    break
        
        return result
