class Solution {
    public int countBattleships(char[][] board) {
        int ans = 0;
        int row = board.length;
        if (row == 0) return 0;
        int column = board[0].length;
        if (column == 0) return 0;
        if (board[0][0] == 'X') ans++;
        for (int i = 1; i < column; i++){
            if (board[0][i] == 'X' && board[0][i-1] != 'X'){
                ans ++;
            }
        }
        
        for (int r = 1; r < row; r++){
            for (int c = 0; c < column; c++){
                if (board[r][c] == 'X'){
                    if (c != 0 && board[r][c-1] != 'X' && board[r-1][c] != 'X') ans++;
                    if (c == 0 && board[r-1][c] != 'X') ans++;
                }
            }
        }
        
        return ans;
    }
}