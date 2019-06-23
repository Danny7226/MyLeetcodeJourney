'''

1091. Shortest Path in Binary Matrix

Medium

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

Example 1:
Input: [[0,1],[1,0]]
Output: 2

Example 2:
Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

'''

grid = [[0,0,1,0,0,0,0],[0,1,0,0,0,0,1],[0,0,1,0,1,0,0],[0,0,0,1,1,1,0],[1,0,0,1,1,0,0],[1,1,1,1,1,0,1],[0,0,1,0,0,0,0]]

class Solution:
    # Breadth First Research
    def shortestPathBinaryMatrix(self, grid: list) -> int:
        if not grid or grid[0][0]==1:
            return -1
        m, n = len(grid[0]), len(grid)

        # Initial Part
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 'B'

        for i in grid:
            print(i)
        print()                    

        visited = [[False]*m for _ in range(n)]
        # print(visited)

        # BFS Part
        queue = []
        queue.append((0,0,0))
        visited[0][0] = True
        around = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        while queue:
            i, j, value = queue.pop(0)
            if grid[i][j] != 'B':
                # print(i,j,grid[i][j])
                grid[i][j] = value + 1
            else:
                continue
            for x, y in around:
                if (0<=i+x<=m-1) and (0<=j+y<=n-1) and visited[i+x][j+y] == False:
                    # print(i+x,j+y)
                    queue.append((i+x, j+y, grid[i][j]))
                    visited[i+x][j+y] = True


        for i in grid:
            print(i)

        if visited[-1][-1] and grid[-1][-1] != 'B':
            return grid[-1][-1]
        else:
            return -1

s = Solution()
print(s.shortestPathBinaryMatrix(grid))            