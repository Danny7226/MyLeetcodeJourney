class Solution {
    public int orangesRotting(int[][] grid) {
        if(grid[0].length == 0) return 0;
        Queue<Integer> qx = new LinkedList<>();
        Queue<Integer> qy = new LinkedList<>();
        Queue<Integer> days = new LinkedList<>();
        int rows = grid.length, columns = grid[0].length;
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < columns; c++){
                if(grid[r][c] == 2){
                    qx.offer(r);
                    qy.offer(c);
                    days.offer(0);
                }
            }
        }
        int day = 0, x = 0, y = 0, nx = 0, ny = 0, range = 0;
        int[] dx = {0,0,1,-1}, dy = {1,-1,0,0};
        while(!qx.isEmpty()){
            range = qx.size();
            for(int i = 0; i < range; i++){
                x = qx.poll();
                y = qy.poll();
                day = days.poll();
                for(int j = 0; j <= 3; j++){
                    nx = x+dx[j];
                    ny = y+dy[j];
                    if(0<=nx && nx<rows && 0<=ny && ny<columns && grid[nx][ny]==1){
                        grid[nx][ny]=2;
                        qx.offer(nx);
                        qy.offer(ny);
                        days.offer(day+1);
                    }
                }
            }
        }
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < columns; c++){
                if(grid[r][c] == 1){
                    return -1;
                }
            }
        }
        return day;
        
    }
}