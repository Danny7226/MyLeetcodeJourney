class Solution {
    Map<Integer, List<Integer>> graph;
    int[] ans;
    int[] status;
    int index;
    int raw = 0, processing = 1, done = 2;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        graph = new HashMap<>();
        index = 0;
        ans = new int[numCourses];
        status = new int[numCourses];
        for(int[] pre: prerequisites){
            graph.putIfAbsent(pre[0], new ArrayList<Integer>());
            graph.get(pre[0]).add(pre[1]);
        }
        for(int i = 0; i < numCourses; i++){
            if(status[i] == raw && !dfs(i)) return new int[0];
        }
        return ans;
    }
    public boolean dfs(Integer node){
        if(status[node] == done) return true;
        if (status[node] == processing) return false;
        int size = graph.containsKey(node) ? graph.get(node).size(): 0;
        // System.out.println(size);
        List<Integer> cur = graph.get(node);
        status[node] = processing;
        for(int i = 0; i < size; i++){
            int child = cur.get(i);
            if(!dfs(child)) return false;
        }
        // System.out.println(index);
        ans[index++] = node;
        status[node] = done;
        return true;
    }
}