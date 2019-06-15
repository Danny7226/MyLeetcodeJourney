'''

47. Permutations II

Medium

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        leng = len(nums)
        def backtrack(comb, step):
            if len(comb) == leng:
                output.append(comb)
            else:
                for i in range(len(step)):
                    if i>0 and step[i] == step[i-1]:
                        continue
                    backtrack(comb + [step[i]], step[:i] + step[i+1:])
        output = []
        backtrack([], nums)
        return output


class Solution:
	# faster
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(index, solu):
            if index == len(nums):
                ans.append(solu.copy())
                return
            usednum = set()
            for i in range(index,len(nums)):
                if solu[i] not in usednum:
                    usednum.add(solu[i])
                    solu[index], solu[i] = solu[i], solu[index]
                    dfs(index + 1, solu)
                    solu[index], solu[i] = solu[i], solu[index]
        dfs(0,nums)
        return ans
                    
                
