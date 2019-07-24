'''
tags: Union Find
959. Regions Cut By Slashes
Medium
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.
(Note that backslash characters are escaped, so a \ is represented as "\\".)
Return the number of regions.
Example 1:
Input:
[
  " /",
  "/ "
]
Output: 2

Example 3:
Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:
Note:
1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
'''
class UF:
    def __init__(self, n):
        self.union = [i for i in range(n)]
        
    def find(self, x):
        if self.union[x] != x:
            self.union[x] = self.find(self.union[x])
        return self.union[x]
        
    def unite(self, a, b):
        self.union[self.find(b)] = self.find(a)

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows, columns = len(grid), len(grid[0])
        uf = UF(rows * columns * 4)
        for row in range(rows):
            for column in range(columns):
                cur = grid[row][column]
                root = 4 * (row * columns + column)
                if cur in '/ ':
                    uf.unite(root+0, root+1)
                    uf.unite(root+2, root+3)
                if  cur in '\ ':
                    uf.unite(root+0, root+2)
                    uf.unite(root+1, root+3)
                if row < rows-1:
                    uf.unite(root+3, root+4*columns)
                if row > 0:
                    uf.unite(root, root-4*columns+3)
                if column < columns-1:
                    uf.unite(root+2, root+4+1)
                if column > 0:
                    uf.unite(root+1, root-4+2)
        return len(set(map(uf.find, range(4*rows*columns))))