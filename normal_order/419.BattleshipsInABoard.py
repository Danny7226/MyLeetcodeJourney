'''

419. Battleships in a Board

Medium

Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

'''

class Solution:
	# one pass, space O(1)
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        ans = 0
        rows, columns = len(board), len(board[0])
        for row in range(rows):
            for column in range(columns):
                if board[row][column] == 'X' and (row == 0 or board[row-1][column] == '.') and (column == 0 or board[row][column-1] == '.'):
                    ans += 1
        return ans

class Solution:
    # DFS, space O(N)
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        ans, visited = 0, set()
        rows, columns = len(board), len(board[0])
        
        def dfs(row, column):
            visited.add((row, column))
            around = [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]
            for r, c in around:
                if 0<=r<rows and 0<=c<columns and board[r][c]=='X' and (r, c) not in visited:
                    dfs(r,c)      
                    
        for row in range(rows):
            for column in range(columns):
                if board[row][column]=='X' and (row, column) not in visited:
                    dfs(row, column)
                    ans += 1
        return ans 
