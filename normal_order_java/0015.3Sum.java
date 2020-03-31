class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);
        int L = nums.length;
        for(int i = 0; i < L-2; i++){
            if(nums[i] + nums[i+1] + nums[i+2] > 0) break;
            if(i > 0 && nums[i] == nums[i-1]) continue;
            if(nums[i] + nums[L-1] + nums[L-2] < 0) continue;
            int lo = i + 1, hi = L-1;
            while(lo < hi){
                int sum = nums[i] + nums[lo] + nums[hi];
                if(sum == 0){
                    ans.add(Arrays.asList(nums[i],nums[lo],nums[hi]));
                    lo++;
                    while(lo < hi && nums[lo] == nums[lo-1]) lo++;
                    hi--;
                    while(lo < hi && nums[hi] == nums[hi+1]) hi--;
                }
                else if(sum < 0){
                    lo++;
                }
                else{
                    hi--;
                }
            }
        }
        
        return ans;
    }
}