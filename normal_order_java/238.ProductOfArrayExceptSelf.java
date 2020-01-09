class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] ans = new int[len];
        ans[0] = nums[0];
        for(int i = 1; i<len; i++){
            ans[i] = ans[i-1] * nums[i];
        }
        int R = 1;
        for(int i = len-1; i>0; i--){
            ans[i] = ans[i-1] * R;
            R *= nums[i];
            // System.out.println(R);
        }
        ans[0] = R;
        return ans;
    }
}

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        left[0] = nums[0];
        right[nums.length - 1] = nums[nums.length-1];
        for(int i = 1; i < nums.length; i++){
            left[i] = left[i-1] * nums[i];
            right[nums.length-1-i] = right[nums.length-i] * nums[nums.length-i-1];
            // System.out.println(left[i]);
            // System.out.println(right[nums.length - 1 - i]);
        }
        int[] ans = new int[nums.length];
        ans[0] = right[1];
        ans[nums.length - 1] = left[nums.length - 2];
        for(int i = 1; i<nums.length-1; i++){
            ans[i] = left[i-1] * right[i+1];
        }
        return ans;
    }
}