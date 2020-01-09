class Solution {
    Map<Integer, Integer> count = new HashMap<>();
    class CustomComparator implements Comparator<Integer>{
        @Override
        public int compare(Integer a, Integer b){
            return count.get(a) - count.get(b);
        }
    }    
    public List<Integer> topKFrequent(int[] nums, int k) {
        for(int num: nums){
            if(count.containsKey(num)) count.put(num, count.get(num)+1);
            else count.put(num, 1);
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(k+1, new CustomComparator());
        for(int key: count.keySet()){
            pq.offer(key);
            if(pq.size()>k) pq.poll();
        }
        List<Integer> ans = new ArrayList<>();
        for(int i = 0; i < k; i++){
            ans.add(pq.poll());
        }
        Collections.reverse(ans);
        return ans;
    }
}
