
1138. Alphabet Board Path
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"].
We may make the following moves:
'U' moves our position up one row, if the square exists;
'D' moves our position down one row, if the square exists;
'L' moves our position left one column, if the square exists;
'R' moves our position right one column, if the square exists;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.
Example 1:
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:
Input: target = "code"
Output: "RR!DDRR!UUL!R!"

class Solution:
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
    def alphabetBoardPath(self, target: str) -> str:
        ans = ''
        x, y = 0, 0
        loc = {}
        for i in 'abcdefghijklmnopqrstuvwxyz':
            loc[i] = (x, y)
            y += 1
            if y > 4:
                x, y = x+1, 0
        ini = 'a'
        # print(loc)
        def find(x1,y1,x2,y2, comb):
            if (x1,y1) == (x2,y2):
                return comb+'!'
            if x1 == 5:
                return find(x1-1,y1,x2,y2,comb+'U')
            if y1 > y2:
                return find(x1,y1-1,x2,y2,comb+'L')
            elif y1 < y2:
                return find(x1,y1+1,x2,y2,comb+'R')
            else:
                if x1 > x2:
                    return find(x1-1,y1,x2,y2,comb+'U')
                else:
                    return find(x1+1,y1,x2,y2,comb+'D')
                
        for letter in target:
            ans+=find(loc[ini][0], loc[ini][1], loc[letter][0], loc[letter][1], '')
            ini = letter
            
        return ans
                    
            