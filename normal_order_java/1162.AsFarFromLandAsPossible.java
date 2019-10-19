class Solution {
    public int maxDistance(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int N = grid.length;
        for(int r = 0; r<N; r++){
            for(int c = 0; c<N; c++){
                if(grid[r][c]==1) q.offer(new int[]{r,c,0});
            }
        }
        if(q.size() == Math.pow(N,2)) return -1;
        int[] cur, dx = {0,0,1,-1}, dy = {1,-1,0,0};
        int range, x, y, nx, ny, dis = -1;
        while(!q.isEmpty()){
            range = q.size();
            for(int i = 0; i < range; i++){
                cur = q.poll();
                x = cur[0];
                y = cur[1];
                dis = cur[2];
                for(int j = 0; j <= 3; j++){
                    nx = x + dx[j];
                    ny = y + dy[j];
                    if(0<=nx && nx<N && 0<=ny && ny<N && grid[nx][ny]==0){
                        grid[nx][ny] = dis+1;
                        q.offer(new int[]{nx,ny,dis+1});
                    }
                }
            }
        }
        return dis;
    }
}