class Solution {
    int[] req;
    Map<Integer, List<Integer>> graph;
    public int minimumSemesters(int N, int[][] relations) {
        req = new int[N+1]; // default 0;
        graph = new HashMap<>();
        for(int[] relation: relations){
            graph.putIfAbsent(relation[0], new ArrayList<>());
            graph.get(relation[0]).add(relation[1]);
            req[relation[1]]++;
        }
        int res = N, ans = 0, cur;
        Queue<Integer> q = new LinkedList<>();
        for(int i = 1; i<= N; i++){
            if(req[i] == 0){
                q.offer(i);
                res--;
            }
            // System.out.println(i);
        }
        while(!q.isEmpty()){
            int size = q.size();
            for(int i = 0; i < size; i++){
                cur = q.poll();
                // System.out.println(cur + " " + req[cur]);
                if(graph.get(cur) != null){
                    int range = graph.get(cur).size();
                    for(int j = 0; j < range; j++){
                        req[graph.get(cur).get(j)]--;
                        if(req[graph.get(cur).get(j)] == 0){
                            q.offer(graph.get(cur).get(j));
                            res--;
                            // System.out.println(cur);
                        }
                    }
                }
            }
            ans++;
        }
        // System.out.print(res);
        return res == 0? ans:-1;
        
        
        
    }
}