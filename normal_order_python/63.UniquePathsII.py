'''

tags: Dynamic Programing

63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

'''
obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        if obstacleGrid[0][0]:
            return 0
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        # print(m,n)
        obstacleGrid[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]

        for i in range(1,n):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]

        print(obstacleGrid)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[j][i]:
                    obstacleGrid[j][i] = 0
                else:
                    obstacleGrid[j][i] = obstacleGrid[j-1][i] + obstacleGrid[j][i-1]
        print(obstacleGrid)
        return obstacleGrid[-1][-1]
s = Solution()
print(s.uniquePathsWithObstacles(obstacleGrid))