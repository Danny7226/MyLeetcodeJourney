'''
tags: BFS

994. Rotting Oranges

Easy

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        queue = [([(i,j) for i in range(rows) for j in range(columns) if grid[i][j] == 2], 0)]
        print(queue)
            
        for rotten, day in queue:
            ans = day
            print(rotten)
            tmp = []
            for r, c in rotten:
                adjacent = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for i, j in adjacent:
                    if 0<=i<rows and 0<=j<columns and grid[i][j] == 1:
                        grid[i][j] = 2
                        tmp.append((i,j))
            if tmp:
                queue.append((tmp, day+1))       
        if any(1 in i for i in grid): # neat statement
            return -1
        return ans
        
        