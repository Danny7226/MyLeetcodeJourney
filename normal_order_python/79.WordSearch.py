'''
tags: backtrack(DFS)

79. Word Search

Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ans = False
        self.word = word
        self.length = len(word)
        if not board:
            return self.ans
        self.rows, self.columns = len(board), len(board[0])
        for row in range(self.rows):
            for column in range(self.columns):     
                if board[row][column] == word[0] and not self.ans:
                    print(self.word[0], end='')
                    prev = board[row][column]
                    board[row][column] = 'X'                    
                    self.helper(board, 1, row, column)
                    board[row][column] = prev
                    print()
                    
        return self.ans
    
    def helper(self, board, index, r, c):
        if index == self.length:
            self.ans = True
            return
        adjacent = [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]
        for (row, column) in adjacent:
            if 0<=row<self.rows and 0<=column<self.columns and board[row][column] == self.word[index]:
                if not self.ans:
                    print(self.word[index], end='')
                    prev = board[r][c] # this matters
                    board[r][c] = 'X'                     
                    self.helper(board, index+1, row, column)
                    board[r][c] = prev