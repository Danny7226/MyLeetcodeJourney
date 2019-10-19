class Solution {
    static int rows;
    static int columns;
    public char[][] updateBoard(char[][] board, int[] click) {
        this.rows = board.length;
        this.columns = board[0].length;
        helper(board, click[0], click[1]);
        return board;
    }
    
    public void helper(char[][] board, int r, int c){
        if(r < 0 || r >= rows || c<0 || c >= columns || board[r][c] == 'B') return;
        if(board[r][c] == 'M'){
            board[r][c] = 'X';
            return;
        }
        int count = 0, x = 0, y = 0;
        int[] dx = {-1,-1,-1,0,0,1,1,1}, dy = {-1,0,1,-1,1,-1,0,1};
        for(int j = 0; j <=7; j++){
            x = r + dx[j];
            y = c + dy[j];
            if(0<=x && x < rows && 0<=y && y< columns && board[x][y]=='M') count++;
        }
        if(count!=0){
            board[r][c] = (char)(count+'0'); // it matters
            return;
        }
        board[r][c] = 'B';
        for(int i=0; i<=7; i++){
            x = r + dx[i];
            y = c + dy[i];            
            helper(board, x, y);
        }
    }
}