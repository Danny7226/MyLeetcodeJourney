class Solution {
    boolean[] visited;
    int[] paint;
    public boolean isBipartite(int[][] graph) {
        visited = new boolean[graph.length];
        paint = new int[graph.length];
        for(int i = 0; i < graph.length; i++){
            if(!visited[i] && !dfs(graph, i, 0)){
                return false;
            }
        }
        return true;
    }
    
    public boolean dfs(int[][] graph, int node, int color){
        if(visited[node]){
            // System.out.println(node + " " + paint);
            return (paint[node] == color);
        }
        else{
            paint[node] = color;
            visited[node] = true;
            for(int i = 0; i < graph[node].length; i++){
                if(!dfs(graph, graph[node][i], 1-color)){
                    return false;
                }
            }
            return true;
        }
    }
    
}