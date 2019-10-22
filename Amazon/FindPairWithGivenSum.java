// Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

// Conditions:

// You will pick exactly 2 numbers.
// You cannot pick the same element twice.
// If you have muliple pairs, select the pair with the largest number.
// Example 1:

// Input: nums = [1, 10, 25, 35, 60], target = 90
// Output: [2, 3]
// Explanation:
// nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
// Example 2:

// Input: nums = [20, 50, 40, 25, 30, 10], target = 90
// Output: [1, 5]
// Explanation:
// nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
// nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
// You should return the pair with the largest number.
// Related problems:
// https://leetcode.com/problems/two-sum

import java.util.*;
public class FindPairWithGivenSum{
	public static void main(String[] args){
		int [] nums = new int[]{20, 50, 40, 25, 30, 10};
		int target = 90;
		int[] ans = Solutions.getAnswer(nums, target);
		System.out.println(ans[0] + " " + ans[1]);
	}
}

class Solutions{
	public static int[] getAnswer(int[] nums, int target){
		Map<Integer, Integer> ht = new HashMap<>();
		int largest = 0, tar = target - 30;
		int[] ans = new int[2];
		for(int i = 0; i < nums.length; i++){
			if(ht.containsKey(nums[i])){
				if(nums[i] > largest || nums[ht.get(nums[i])] > largest){
					ans[0] = ht.get(nums[i]);
					ans[1] = i;
					largest = Math.max(nums[i], nums[ht.get(nums[i])]);
				}
			}
			ht.put(tar - nums[i], i);
		}
		return ans;

	}
}