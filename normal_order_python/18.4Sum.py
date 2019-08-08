'''

tag: hash_table, 2 ptrs

18. 4Sum

Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


'''
nums = [-1,-5,-5,-3,2,5,0,4]
target =-7

# class Solution:
#     def fourSum(nums: list, target: int) -> list:
#         nums.sort()
#         print(nums)
#         output = []
        
#         def threesum(target, nums):
#             last_three = []
#             for i in range(len(nums)-2):
#                 if i != 0 and nums[i] == nums[i-1]:
#                     continue
#                 minsum = nums[i] + nums[i+1] + nums[i+2]
#                 maxsum = nums[i] + nums[-1] + nums[-2]
#                 if minsum > target:
#                     return last_three
#                 if maxsum < target:
#                     continue
                    
#                 l, r = i+1, len(nums)-1
#                 while l<r:
#                     tmp = nums[i] + nums[l] + nums[r]
#                     if tmp < target:
#                         l +=1
#                     elif tmp >target:
#                         r -=1
#                     else:
#                         last_three.append([nums[i],nums[l],nums[r]])

#                         while l<r and nums[l] == nums[l+1]:
#                             l+=1
#                         while l<r and nums[r] == nums[r-1]:
#                             r-=1
#                         l += 1
#                         r -= 1
#             return last_three
                            
            
#         for i in range(len(nums)-3):
#             tmp = target - nums[i]
#             last_three = threesum(tmp, nums[i+1:])
#             print('last_three:',last_three)
#             if len(last_three) == 0:
#                 continue
#             else:
#                 for j in last_three:
#                     four = [nums[i]] + j
#                     if not four in output:
#                         output.append([nums[i]]+j)
#         return output


def fourSum(self, nums, target):

	# NSum solution with recursion

    def findNsum(l, r, target, N, result, results):
        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums)-1, target, 4, [], results)
    return results

# def fourSum(self, nums, target):
#
#     # same as above, but recursion by passing slice list not 2ptrs
#
#     def findNsum(nums, target, N, result, results):
#         if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
#             return
#         if N == 2: # two pointers solve sorted 2-sum problem
#             l,r = 0,len(nums)-1
#             while l < r:
#                 s = nums[l] + nums[r]
#                 if s == target:
#                     results.append(result + [nums[l], nums[r]])
#                     l += 1
#                     while l < r and nums[l] == nums[l-1]:
#                         l += 1
#                 elif s < target:
#                     l += 1
#                 else:
#                     r -= 1
#         else: # recursively reduce N
#             for i in range(len(nums)-N+1):
#                 if i == 0 or (i > 0 and nums[i-1] != nums[i]):
#                     findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

#     results = []
#     findNsum(sorted(nums), target, 4, [], results)
#     return results

print(Solution.fourSum(nums,target))        