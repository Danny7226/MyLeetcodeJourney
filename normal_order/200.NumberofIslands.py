'''

tags: BFS DFS Union-Find

200. Number of Islands

Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

class Solution:
    # dfs
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ans, visited = 0, set()
        rows, columns = len(grid), len(grid[0])
        
        def dfs(row, column):
            visited.add((row, column))
            around = [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]
            for r, c in around:
                if 0<=r<rows and 0<=c<columns and grid[r][c]=='1' and (r, c) not in visited:
                    dfs(r,c)      
                    
        for row in range(rows):
            for column in range(columns):
                if grid[row][column]=='1' and (row, column) not in visited:
                    dfs(row, column)
                    ans += 1
        return ans   

class Solution:
    # bfs
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ans, seen = 0, set()
        rows, columns = len(grid), len(grid[0])
                    
        for row in range(rows):
            for column in range(columns):
                if grid[row][column]=='1' and (row, column) not in seen:
                    # bfs starts
                    seen.add((row,column))
                    queue = [(row, column)]
                    for (r, c) in queue:
                        around = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                        for i, j in around:
                            if 0<=i<rows and 0<=j<columns and grid[i][j]=='1' and (i, j) not in seen:
                                    queue.append((i,j))
                                    seen.add((i,j))
                    # bfs ends
                    ans += 1
        return ans                    
                    
