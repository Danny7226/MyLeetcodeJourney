'''
tags: Trie DFS
212. Word Search II
Hard
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
Example:
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie, self.ans = {}, set()
        rows, columns = len(board), len(board[0])
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['#'] = None
        
        def dfs(trie, x, y, comb):
            node = board[x][y]
            if node in trie:
                adj = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                nxt = trie[node]
                board[x][y] = '.'
                comb = comb+node
                if '#' in nxt:
                    self.ans.add(comb)                
                for i, j in adj:
                    if 0<=i<rows and 0<=j<columns:
                        dfs(nxt, i, j, comb)
                board[x][y] = node

        for row in range(rows):
            for column in range(columns):
                dfs(trie, row, column, '')
        return list(self.ans)