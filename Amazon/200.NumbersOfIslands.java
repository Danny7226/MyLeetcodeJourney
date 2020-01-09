class Solution {
    char[][] grid;
    int rows;
    int columns;
    public int numIslands(char[][] grid) {
        if(grid.length == 0) return 0;
        int ans = 0;
        this.grid = grid;
        rows = grid.length;
        columns = grid[0].length;
        for(int row = 0; row < rows; row++){
            for(int column = 0; column < columns; column++){
                if(grid[row][column] == '1'){
                    dfs(row, column);
                    ans++;
                }
            }
        }
        return ans;
    }
    
    public void dfs(int row, int column){
        if(row<0 || row>=rows || column<0 || column >= columns) return;
        if(grid[row][column] == '0') return;
        grid[row][column] = '0';
        int[] dx = new int[]{0,0,1,-1};
        int[] dy = new int[]{1,-1,0,0};
        for(int i = 0; i<4; i++){
            dfs(row+dx[i], column+dy[i]);
        }
    }
}