class Solution {
    Map<Integer, List<Integer>> graph;
    int[] ans;
    boolean[] seen;
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        graph = new HashMap<>();
        ans = new int[quiet.length];
        seen = new boolean[quiet.length];
        for(int n = 0; n < quiet.length; n++){
            ans[n] = n;
        }
        for(int[] rich: richer){
            graph.putIfAbsent(rich[1], new ArrayList<>());
            graph.get(rich[1]).add(rich[0]);
        }
        for(int i = 0; i < quiet.length; i++){
            dfs(i, quiet);
        }
        return ans;
    }
    
    public void dfs(int node, int[] quiet){
        if(seen[node]) return;
        if(graph.containsKey(node)){
            List<Integer> cur = graph.get(node);
            int size = cur.size();
            for(int i = 0; i < size; i++){
                dfs(cur.get(i), quiet);
                ans[node] = quiet[ans[cur.get(i)]] < quiet[ans[node]]? ans[cur.get(i)] : ans[node];
            }
            // System.out.println(node + " " + ans[node]);
        }
        else{
            ans[node] = node;
            // System.out.println(node + " " + ans[node]);
        }
        seen[node] = true;
    }
}