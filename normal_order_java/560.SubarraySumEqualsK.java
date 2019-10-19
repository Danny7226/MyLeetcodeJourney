class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> pair = new HashMap<>();
        pair.put(0, 1);
        int sum = 0, ans = 0;
        for(int i: nums){
            sum += i;
            if(pair.containsKey(sum - k)) ans += pair.get(sum-k);
            pair.put(sum, pair.getOrDefault(sum, 0)+1);            
        }
        return ans;
    }
}