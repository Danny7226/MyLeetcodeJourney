'''

40. Combination Sum II

Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''

candidates, target = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], 27

class Solution:
    # 40ms fastest method
    def combinationSum2(self, candidates: list, target: int) -> list:
        output = []
        candidates.sort()
        def backtrack(comb, target, start):
            if target == 0:
                output.append(comb)
            else:                
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    elif candidates[i] > target:
                        break
                    else:
                        backtrack(comb + [candidates[i]], target - candidates[i], i+1)
        backtrack([], target, 0)
        return output

# class Solution:
#     # slower
#     def combinationSum2(self, candidates: list, target: int) -> list:
#         output = []
#         candidates.sort()
#         def backtrack(comb, target, candidates):
#             if target == 0:
#                 if comb not in output:
#                     output.append(comb)
#             else:
#                 if candidates == [] or target< candidates[0]:
#                     return                
#                 for i, num in enumerate(candidates):
#                     backtrack(comb + [num], target - num, candidates[i+1:])
#         backtrack([], target, candidates)
#         return output

s = Solution()
print(s.combinationSum2(candidates, target))