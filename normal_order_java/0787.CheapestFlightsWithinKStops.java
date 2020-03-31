class CustomComp implements Comparator<int[]>{
    public int compare(int[] a, int[] b){
        return a[0] - b[0];
    }
}
class Solution {
    ArrayList<int[]>[] graph;
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        graph = new ArrayList[n];
        for(int i = 0; i < n; i++){
            graph[i] = new ArrayList<>();
        }
        for(int[] flight: flights){
            graph[flight[0]].add(new int[]{flight[1], flight[2]});
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>(new CustomComp());
        pq.offer(new int[]{0, src, K+1});
        while(!pq.isEmpty()){
            int[] cur = pq.poll();
            if(cur[1] == dst) return cur[0];
            if(cur[2]>0){
                for(int[] nxt: graph[cur[1]]){
                    pq.offer(new int[]{cur[0]+nxt[1], nxt[0], cur[2]-1});
                }
            }
        }
        return -1;
    }
}