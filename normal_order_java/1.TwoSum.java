class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hm = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(hm.containsKey(nums[i])) {
                return new int[]{hm.get(nums[i]), i};
            }            
            int k = target - nums[i];
            hm.put(k, i);
        }
        return null;
    }
}