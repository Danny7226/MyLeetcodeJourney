class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        // count
        Map<String, Integer> count = new HashMap<>();
        for(String word: words){
            if(count.containsKey(word)) count.put(word, count.get(word)+1);
            else count.put(word, 1);
        }
        // heap setup
        PriorityQueue<String> pq = new PriorityQueue<>((s1, s2)->{
            int result = count.get(s1) - count.get(s2);
            if(result != 0) return result;
            return s2.compareTo(s1);
        });
        for(String key: count.keySet()){
            pq.offer(key);
            if(pq.size()>k) pq.poll();
        }
        List<String> ans = new ArrayList<>();
        while(!pq.isEmpty()){
            ans.add(pq.poll());
        }
        Collections.reverse(ans);
        return ans;
    }
}