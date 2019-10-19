class Comp implements Comparator<Integer>{
    public int compare(Integer a, Integer b){
        return a-b;
    }
}
class Solution {
    List<Integer> ans;
    int[] status;
    int raw = 0, processing = 1, safe = 2;
    public List<Integer> eventualSafeNodes(int[][] graph) {
        ans = new ArrayList<Integer>();
        status = new int[graph.length];
        for(int i = 0; i < graph.length; i++){
            if(status[i] == raw){
                dfs(graph, i);
            }
        }
        Collections.sort(ans, new Comp());
        return ans;
    }
    
    public boolean dfs(int[][] graph, int node){
        if(status[node] == safe) return true;
        if(status[node] == processing) return false;
        int[] cur = graph[node];
        status[node] = processing;
        for(int i = 0; i < cur.length; i++){
            if(!dfs(graph, cur[i])){
                return false;
            }
        }
        status[node] = safe;
        ans.add(node);
        return true;
    }
}