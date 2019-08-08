'''
416. Partition Equal Subset Sum
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse = True)
        target, reminder = divmod(sum(nums), 2)
        if reminder or max(nums) > target: return False # O(N)
        # print(target, reminder)
        def helper(index, cur_sum):
            if cur_sum > target: return
            if cur_sum == target:
                return True
            for i in range(index, len(nums)):
                if helper(i+1, cur_sum+nums[i]):
                    return True
            return False
        return helper(0, 0)