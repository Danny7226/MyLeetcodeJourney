candidates, target = [8,7,4,3], 11

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