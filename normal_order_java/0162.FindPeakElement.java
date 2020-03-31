class Solution {
    public int findPeakElement(int[] nums) {
        int lo = 0, hi = nums.length-1;
        if(hi == 0) return 0;
        while(lo < hi){
            int mid = (lo + hi) / 2;
            // System.out.println(mid);
            if(nums[mid]<nums[mid+1]) lo = mid+1;
            else hi = mid;
        }
        return lo;
    }
}