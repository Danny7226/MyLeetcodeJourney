class Solution {
    int rows, columns;
    boolean[][] seen;
    public int numDistinctIslands(int[][] grid) {
        this.rows = grid.length;
        this.columns = grid[0].length;
        seen = new boolean[rows][columns];
        Set<List<Character>> ans = new HashSet<>();
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < columns; c++){
                if(grid[r][c]==1 && !seen[r][c]){
                    List<Character> shape = new ArrayList<>();
                    dfs(grid, r, c, shape, '0');
                    // System.out.println(shape);
                    ans.add(shape);
                }
            }
        }
        return ans.size();
    }
    
    public void dfs(int[][] grid, int r, int c, List<Character> shape, char dir){
        shape.add(dir);
        if(0<=r && r<rows && 0<=c && c<columns && grid[r][c] == 1 && !seen[r][c]){
            seen[r][c] = true;
            dfs(grid, r+1, c, shape, 'd');
            dfs(grid, r-1, c, shape, 'u');
            dfs(grid, r, c+1, shape, 'r');
            dfs(grid, r, c-1, shape, 'l');
        }
    }
}