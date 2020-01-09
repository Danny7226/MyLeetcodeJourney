class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        if(nums.length < 3) return ans; // matters
        Arrays.sort(nums);
        for(int i = 0; i < nums.length-2; i++){ // i<nums.length-2 matters
            int l = i + 1, r = nums.length-1;
            if(nums[i] + nums[l] + nums[l+1] > 0) break;
            if(nums[i] + nums[r] + nums[r-1] < 0) continue;
            if(i > 0 && nums[i] == nums[i-1]) continue;
            while(l < r){
                if(nums[i] + nums[l] + nums[r] > 0) r--;
                else if(nums[i] + nums[l] + nums[r] < 0) l++;
                else{
                    ans.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                    while(l<r && nums[l] == nums[l-1]) l++; //maters
                    while(l<r && nums[r] == nums[r+1])r--; //maters
                }
            }
        }
        return ans;
    }
}