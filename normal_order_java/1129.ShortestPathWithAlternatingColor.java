class Solution {
    int red = 1, blue = 2, root = 0;
    Set<String> seen;
    public int[] shortestAlternatingPaths(int n, int[][] red_edges, int[][] blue_edges) {
        int[] ans = new int[n];
        seen = new HashSet<>();
        Arrays.fill(ans, -1);
        Map<Integer, List<Integer>> red_e = new HashMap<>(), blue_e = new HashMap<>();
        for(int[] edge: red_edges){
            red_e.putIfAbsent(edge[0], new ArrayList<Integer>()); 
            red_e.get(edge[0]).add(edge[1]);
        }
        for(int[] edge: blue_edges){
            blue_e.putIfAbsent(edge[0], new ArrayList<Integer>());  
            blue_e.get(edge[0]).add(edge[1]);
        }
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0,0,0});
        while(!q.isEmpty()){
            int size = q.size();
            for(int i = 0; i < size; i++){
                int[] cur = q.poll();
                String key = cur[0] + " " + cur[1];
                if(seen.contains(key)) continue;
                seen.add(key);
                if(ans[cur[0]] == -1) ans[cur[0]] = cur[2];
                if(cur[1] == red || cur[1] == root){
                    if(blue_e.containsKey(cur[0])){
                        for(int child: blue_e.get(cur[0])) q.offer(new int[]{child, blue, cur[2]+1});
                    }
                }
                if(cur[1] == blue || cur[1] == root){
                    if(red_e.containsKey(cur[0])){
                        for(int child: red_e.get(cur[0])) q.offer(new int[]{child, red, cur[2]+1});
                    }
                }
            }
      }
      return ans;
    }
}