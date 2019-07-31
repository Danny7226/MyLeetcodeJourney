'''
tags: DP DFS
698. Partition to K Equal Sum Subsets
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:
1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, reminder = divmod(sum(nums), k)
        if reminder or max(nums) > target: return False
        visited = [False] * len(nums)
        def DFS(k, index, cur_sum):
            print(cur_sum, index, end=' ')
            if k == 0:
                return True
            if cur_sum == target:
                return DFS(k-1, 0, 0)
            for i in range(index, len(nums)):
                # print(i)
                if cur_sum + nums[i] <= target and not visited[i]:
                    visited[i] = True
                    # print(i)
                    if DFS(k, i+1, cur_sum+nums[i]):
                        return True
                    visited[i] = False
            return False
            
            
        return DFS(k, 0, 0)