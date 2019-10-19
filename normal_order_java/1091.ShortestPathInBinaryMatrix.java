class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        if(grid[0][0]==1) return -1;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0,0,1});
        int range = 0, path = 0, x = 0, y = 0, nx = 0, ny = 0, N = grid.length;
        int[] cur;
        int[] dx = {-1,-1,-1,0,0,1,1,1}, dy = {-1,0,1,-1,1,-1,0,1};
        while(!q.isEmpty()){
            range = q.size();
            for(int i = 0; i < range; i++){
                cur = q.poll();
                x = cur[0];
                y = cur[1];
                path = cur[2];
                if(x==N-1 && y==N-1) return path;
                for(int j = 0; j <= 7; j++){
                    nx = x+dx[j];
                    ny = y+dy[j];
                    if(0<=nx && nx<N && 0<=ny && ny<N && grid[nx][ny]==0){
                        grid[nx][ny] = 1;
                        q.offer(new int[]{nx, ny, path+1});
                    }
                }                
            }
        }
        return -1;
    }
}