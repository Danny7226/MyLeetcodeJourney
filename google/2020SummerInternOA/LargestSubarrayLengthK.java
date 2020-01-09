import java.util.*;
public class LargestSubarrayLengthK{
	public static void main(String[] args){
		Solutions s = new Solutions();
		int[] nums = new int[]{12,3,1,21,2,52,3};
		int k = 3;
		int[] ans = s.getAnswer(nums, k);
		for(int i = 0; i < k; i++){
			System.out.print(ans[i] + " ");
		}
		System.out.println();
	}
}

class Solutions{
	public int[] getAnswer(int[] nums, int k){
		if(k > nums.length) return new int[]{};
		int max_index = 0;
		for(int i = 0; i <= nums.length - k; i++){
			if(nums[i] > nums[max_index]) {
				max_index = i;
			}
			else if(nums[i] == nums[max_index]){
				if(compare(nums, k, i, max_index) == 1){
					max_index = i;
				}
			}
		}
		int[] ans = new int[k];
		for(int i = 0; i < k; i++){
			ans[i] = nums[max_index + i];
		}
		return ans;
	}
	private int compare(int[] nums, int k, int i, int j){
		for(int index = 0; index < k; index++){
			if(nums[i+index] == nums[j+index]) continue;
			else if (nums[i+index] > nums[j+index]) return 1;
			else return -1;
		}
		return 0;
	}
}