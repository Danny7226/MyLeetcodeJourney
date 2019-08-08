candidates, target = [8,7,4,3], 11

'''

39. Combination Sum

Medium

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''
# class Solution:
#     def combinationSum(self, candidates: list, target: int) -> list:
        
#         output = []
#         candidates.sort()
#         min_step = candidates[0]


#         def backtrack(comb, res):
#             if res == 0 and sorted(comb) not in output:                
#                 output.append(comb)
#             else:
#                 if res < min_step:
#                     return
#                 else:
#                     for i in candidates:
#                         backtrack(comb + [i], res - i)
#         backtrack([], target)
#         return output

class Solution:
    # faster
    def combinationSum(self, candidates: list, target: int) -> list:
        
        output = []
        candidates.sort()

        def backtrack(comb, res, candidates):
            if res == 0:                
                output.append(comb)
            else:
                if res < candidates[0]:
                    return
                else:
                    for i, num in enumerate(candidates):
                        backtrack(comb + [num], res - num, candidates[i:])
        backtrack([], target, candidates)
        return output

s= Solution()
print(s.combinationSum(candidates, target))        