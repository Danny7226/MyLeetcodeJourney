'''
tags: Backtrack
77. Combinations
Medium
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    # backtrack
    def combine(self, n: int, k: int) -> List[List[int]]:
        choices = [n for n in range(1, n + 1)]
        ans = []
        def helper(k, choices, comb):
            if len(comb) == k:
                ans.append(comb)
            else:
                for i in range(len(choices)):
                    helper(k, choices[i+1:], comb+[choices[i]])
        helper(k, choices, [])
        return ans