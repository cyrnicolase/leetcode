# https://leetcode.com/problems/toeplitz-matrix/description/


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        xLen = len(matrix)
        yLen = len(matrix[0])
        
        # up
        for yi in range(0, yLen):
            xi = 0
            v = matrix[xi][yi]
            
            while xi < xLen-1 and yi < yLen-1:
                xi += 1
                yi += 1
                if matrix[xi][yi] != v:
                    return False
        # down     
        for xi in range(1, xLen):
            yi = 0
            v = matrix[xi][yi]
            
            while xi < xLen-1 and yi < yLen-1:
                xi += 1
                yi += 1
                if matrix[xi][yi] != v:
                    return False
                
        return True
       
        
