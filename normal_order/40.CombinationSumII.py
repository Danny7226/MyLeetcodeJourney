'''


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