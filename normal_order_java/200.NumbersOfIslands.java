class Solution {    
    int row;
    int column;  
    public void dfs(char[][] grid, int x, int y){
        if(x<0 || x>=this.row || y<0 || y>=this.column) return;
        if(grid[x][y]== '1'){
            // System.out.println(x + " " + y);
            grid[x][y] = 'x';
            dfs(grid, x+1, y);
            dfs(grid, x-1, y);
            dfs(grid,x,y+1);
            dfs(grid,x,y-1);
        }
    }
    
    public int numIslands(char[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) return 0;
        this.row = grid.length;
        this.column = grid[0].length;
        int ans = 0;
        for(int r=0; r < row; r++){
            for(int c=0; c < column; c++){
                if(grid[r][c]=='1'){
                    // System.out.println();
                    // System.out.println(r + " " + c);
                    dfs(grid, r, c);
                    ans++;   
                }
            }
        }
        return ans;
    }
}