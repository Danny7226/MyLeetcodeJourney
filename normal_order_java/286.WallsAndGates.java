class Solution { // BFS
    public void wallsAndGates(int[][] rooms) {
        if(rooms.length == 0) return;
        int INF = 2147483647, rows = rooms.length, columns = rooms[0].length;
        Queue<int[]> q = new LinkedList<>();
        boolean[][] seen = new boolean[rows][columns];
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < columns; c++){
                if(rooms[r][c] == 0){
                    q.offer(new int[]{r, c, 0});
                    seen[r][c] = true;
                }
            }
        }
        int[] dx = {0, 0, 1, -1}, dy = {1, -1, 0, 0};
        while(!q.isEmpty()){
            int size = q.size();
            for(int i = 0; i < size; i++){
                int[] cur = q.poll();
                for(int j = 0; j <= 3; j++){
                    int nx = cur[0] + dx[j], ny = cur[1] + dy[j];
                    if(0<=nx && nx<rows && 0<=ny && ny<columns && rooms[nx][ny] == INF && !seen[nx][ny]){
                        seen[nx][ny] = true;
                        rooms[nx][ny] = cur[2]+1;
                        q.offer(new int[]{nx, ny, rooms[nx][ny]});
                    }
                }
            }
        }
    }
}