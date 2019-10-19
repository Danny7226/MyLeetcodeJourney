class Solution {
    public int rob(int[] nums) {
        int N = nums.length;
        if(N == 0) return 0;
        int[] ans = new int[N+1];
        ans[0] = 0;
        ans[1] = nums[0];
        for(int i = 2; i <= N; i++){
            ans[i] = Math.max(ans[i-1], ans[i-2] + nums[i-1]);
        }
        return ans[N];
    }
}