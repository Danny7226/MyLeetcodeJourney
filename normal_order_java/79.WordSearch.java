class Solution {
    int columns, rows;
    boolean ans;
    String word;
    public boolean exist(char[][] board, String word) {
        // if(board == null || board[0] == null) return false;
        this.ans = false;
        this.word = word;
        this.rows = board.length;
        this.columns = board[0].length;
        for(int row = 0; row < rows; row++){
            for(int column = 0; column < columns; column++){
                if(board[row][column] == word.charAt(0) && ans == false){
                    board[row][column] = '#';       
                    dfs(board, 1, row, column);
                    board[row][column] = word.charAt(0);
                    // System.out.println();
                }
            }
        }
        return ans;
    }
    
    public void dfs(char[][] board, int index, int r, int c){
        if(index == word.length()){
            ans = true;
            return;
        }
        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};
        for(int i = 0; i<=3; i++ ){
            int x = r+dr[i], y = c+dc[i];
            if(0<=x && x<rows && 0<=y && y<columns && board[x][y] == word.charAt(index) && ans == false){
                board[x][y] = '#';                    
                dfs(board, index+1, x, y);
                board[x][y] = word.charAt(index);                
            }
        }
    }
}

class Solution {
    int columns, rows;
    boolean ans;
    String word;
    static boolean[][] visited;
    public boolean exist(char[][] board, String word) {
        // if(board == null || board[0] == null) return false;
        visited = new boolean[board.length][board[0].length];
        this.ans = false;
        this.word = word;
        this.rows = board.length;
        this.columns = board[0].length;
        for(int row = 0; row < rows; row++){
            for(int column = 0; column < columns; column++){
                if(board[row][column] == word.charAt(0) && ans == false){
                    // System.out.print(word.charAt(0));
                    visited[row][column] = true;
                    dfs(board, 1, row, column);
                    visited[row][column] = false;
                    // System.out.println();
                }
            }
        }
        return ans;
    }
    
    public void dfs(char[][] board, int index, int r, int c){
        if(index == word.length()){
            ans = true;
            return;
        }
        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};
        for(int i = 0; i<=3; i++ ){
            int x = r+dr[i], y = c+dc[i];
            if(0<=x && x<rows && 0<=y && y<columns && board[x][y] == word.charAt(index) && ans == false && visited[x][y] == false){
                // System.out.print(word.charAt(index));
                visited[x][y] = true;
                dfs(board, index+1, x, y);
                visited[x][y] = false;               
            }
        }
    }
}

public class WordSearch{
    public static void main(String[] args){
        char[][] board = {{'b','a','a','b','a','b'},{'a','b','a','a','a','a'},{'a','b','a','a','a','b'},{'a','b','a','b','b','a'},{'a','a','b','b','a','b'},{'a','a','b','b','b','a'},{'a','a','b','a','a','b'}};
        String word = "ababaababaaabbabbaabbaabbaba";
        Solution s = new Solution();
        System.out.println(s.exist(board, word));
    }
}