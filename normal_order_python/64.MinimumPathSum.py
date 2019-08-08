'''

tags: Dynamic Programing

64. Minimum Path Sum

Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

'''
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(1, rows):
            grid[r][0] += grid[r-1][0]
        
        for c in range(1, cols):
            grid[0][c] += grid[0][c-1]
            
        for r in range(1, rows):
            for c in range(1, cols):     
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
                
        return grid[-1][-1]  
              
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        m, n = len(grid[0]), len(grid)
        output = [[0]*m for _ in range(n)]
        output[0][0] = grid[0][0]
        for i in range(1, m):
            output[0][i] = output[0][i-1] + grid[0][i]
        for i in range(1, n):
            output[i][0] = output[i-1][0] + grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                output[j][i] = min(grid[j][i]+output[j-1][i], grid[j][i]+output[j][i-1])
        # print(output)
        return output[-1][-1]        