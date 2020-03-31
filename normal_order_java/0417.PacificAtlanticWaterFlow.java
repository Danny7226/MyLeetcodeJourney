class Solution {
    boolean[][] paci;
    boolean[][] atla;
    boolean[][] visited;
    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if(matrix.length == 0) return ans;
        int rows = matrix.length, columns = matrix[0].length;
        paci = new boolean[rows][columns];
        atla = new boolean[rows][columns];
        Queue<int[]> pq = new LinkedList<>(), aq = new LinkedList<>();
        for(int i = 0; i < rows; i++){
            paci[i][0] = true;
            pq.offer(new int[]{i, 0});
            atla[i][columns-1] = true;
            aq.offer(new int[]{i, columns-1});
        }
        for(int i = 1; i < columns-1; i++){
            paci[0][i] = true;
            pq.offer(new int[]{0, i});
            atla[rows-1][i] = true;
            aq.offer(new int[]{rows-1, i});
        }
        pq.offer(new int[]{0, columns-1});
        paci[0][columns-1] = true;
        aq.offer(new int[]{rows-1, 0});
        atla[rows-1][0] = true;
        bfs(matrix, paci, pq, rows, columns);
        bfs(matrix, atla, aq, rows, columns);
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < columns; c++){
                if(paci[r][c] && atla[r][c]){
                    List<Integer> tmp = new ArrayList<>();
                    tmp.add(r);
                    tmp.add(c);
                    ans.add(tmp);
                }
            }
        }
        return ans;
    }
    
    public void bfs(int[][] matrix, boolean[][] ocean, Queue<int[]> q, int rows, int columns){
        int[] dr = {0, 0, 1, -1}, dc = {1, -1, 0, 0};
        int nr, nc;
        while(!q.isEmpty()){
            int size = q.size();
            for(int i = 0; i < size; i++){
                int[] cur = q.poll();
                for(int j = 0; j < 4; j++){
                    nr = cur[0] + dr[j];
                    nc = cur[1] + dc[j];
                    if(0<=nr && nr<rows && 0<=nc && nc<columns && matrix[nr][nc] >= matrix[cur[0]][cur[1]] && !ocean[nr][nc]){
                        ocean[nr][nc] = true;
                        q.offer(new int[]{nr, nc});
                    }
                }
            }
        }
    }
}