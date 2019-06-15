'''

tags: backtrack

46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

class Solution:
    def permute(self, nums: list) -> list:
        step = set(nums)
        
        def backtrack(step, comb):
            if not step:
                output.append(comb)
            else:
                for i in step:
                    backtrack(step - {i}, comb + [i])
                
        output = []
        backtrack(step, [])
        return output

# a = [1,2,3]
# def check(a):
#     a.append(4)
#     return a 
# b = check(a)
# print(a) # [1,2,3,4]
