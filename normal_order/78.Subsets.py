'''
78. Subsets
Medium
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        def helper(k, choices, comb):
            if len(comb) == k:
                ans.append(comb)
            else:
                for i in range(len(choices)):
                    helper(k, choices[i+1:], comb+[choices[i]])
        for j in range(n+1):
            helper(j, nums, [])
        return ans