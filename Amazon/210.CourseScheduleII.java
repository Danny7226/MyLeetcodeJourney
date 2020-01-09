class Solution {
    int index;
    int[] status;
    int[] ans;
    Map<Integer, LinkedList<Integer>> graph;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        if(numCourses == 0) return new int[]{};
        index = 0;
        graph = new HashMap<>();
        ans = new int[numCourses];
        for(int i = 0; i < numCourses; i++){
            graph.put(i, new LinkedList<Integer>());
        }
        status = new int[numCourses];
        Arrays.fill(status, -1); // -1 means unvisted, 0 means visiting, 1 means visited
        // build graph
        for(int[] pre: prerequisites){
            graph.get(pre[0]).add(pre[1]);
        }
        // dfs     
        for(int i = 0; i < numCourses; i++){
            if(status[i] == -1){
                // System.out.println(i);
                if(!dfs(i)){
                    return new int[]{};
                }
            }
        }   
        return ans;
    }
    public boolean dfs(int i){
        if(status[i] == 0) return false;
        if(status[i] == 1) return true;
        status[i] = 0;
        List<Integer> neighbors = graph.get(i);
        for(int j = 0; j<neighbors.size(); j++){
            if(!dfs(neighbors.get(j))){
                return false;
            }
        }            
        status[i] = 1;
        // System.out.println(i);
        ans[index++] = i;
        return true;
    }     
    
}