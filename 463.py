
# https://leetcode.com/problems/island-perimeter/description/


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        '''
        每个单元格都是被4 条边包围着
        如果被包围的是陆地,那么就少了一条边
        '''
        
        yLen = len(grid)
        xLen = len(grid[0])
        
        sum = 0
        for y in range (0, yLen):
            for x in range (0, xLen):
                if 1 == grid[y][x]:
                    sum += self.unitPerimeter(x, y, xLen, yLen, grid)
        
        return sum
                    
      
    def unitPerimeter(self, x, y, xLen, yLen, grid):
        '''
        这里就是判断陆地单元格周围单元格类型,如果是陆地,那么就少一个边界
        '''
        perimeter = 4
        if x - 1 >= 0 and 1 == grid[y][x-1]:
            perimeter -= 1
        if x + 1 < xLen and 1 == grid[y][x+1]:
            perimeter -= 1
        if y - 1 >= 0 and 1 == grid[y-1][x]:
            perimeter -= 1
        if y + 1 < yLen and 1 == grid[y+1][x]:
            perimeter -= 1
            
        return perimeter
            
