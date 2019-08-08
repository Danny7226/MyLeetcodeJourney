'''

tags: hash table

36. Valid Sudoku

Medium

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.

'''
class Solution:
	# better one
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_row = [set() for i in range(9)]
        # hash_row = [set()] * 9 does not work, cuz it generate 9 set()
        # with same address then these 9 sets will change together.
        hash_col = [set() for i in range(9)]
        hash_square = [[set() for i in range(3)] for i in range(3)]
        
        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                # print(row, col)
                if cur != '.':
                    if cur not in hash_row[row]:
                        hash_row[row].add(cur)
                    else:
                        # print(1)
                        return False
                    if cur not in hash_col[col]:
                        hash_col[col].add(cur)
                    else:
                        # print(2)
                        return False
                    if cur not in hash_square[row//3][col//3]:
                        hash_square[row//3][col//3].add(cur)
                    else:
                        # print(3)
                        return False
        return True

# class Solution:
#     def isValidSudoku(self, board: list) -> bool:
#         table = [
#             board[0][0:3]+board[1][0:3]+board[2][0:3],
#             board[3][0:3]+board[4][0:3]+board[5][0:3],
#             board[6][0:3]+board[7][0:3]+board[8][0:3],
#             board[0][3:6]+board[1][3:6]+board[2][3:6],
#             board[3][3:6]+board[4][3:6]+board[5][3:6],
#             board[6][3:6]+board[7][3:6]+board[8][3:6],
#             board[0][6:9]+board[1][6:9]+board[2][6:9],
#             board[3][6:9]+board[4][6:9]+board[5][6:9],
#             board[6][6:9]+board[7][6:9]+board[8][6:9],            
#         ]                    
#         zipped = zip(
# board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]
#         ) 
        
#         for i in zipped:
#             hash1 = set()
#             for j in i:
#                 if j == '.':
#                     continue
#                 elif j not in hash1:
#                     hash1.add(j)
#                 else:
#                     return False
                        
#         for i in board:
#             hash2 = set()
#             for j in i:
#                 if j == '.':
#                     continue                
#                 if j not in hash2:
#                     hash2.add(j)
#                 else:
#                     return False            

#         for i in table:
#             hash3 = set()
#             for j in i:
#                 if j == '.':
#                     continue
#                 elif j not in hash3:
#                     hash3.add(j)
#                 else:
#                     return False                       
        
#         return True


a = [[set()]*3] * 3
print(a)      