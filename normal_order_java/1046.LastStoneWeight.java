class Solution {
    class Compare implements Comparator<Integer>{
        public int compare(Integer a, Integer b){
            return b-a;
        }
    }
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(new Compare());
        for(int s: stones){
            pq.offer(s);
        }
        while(pq.size()>1){
            int cur = pq.poll()-pq.poll();
            if(cur != 0) pq.offer(cur);
        }
        return pq.size()==1 ? pq.poll() : 0;
    }
}