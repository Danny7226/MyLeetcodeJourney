'''

tags: 2 pointers

15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
Accepted
528,302
Submissions
2,218,611

'''
l = [-1,0,1]

# d = {'a':1, 'b':2}
# for i, key in enumerate(d):
# 	print(i,key, end = '    {0}.'.format(key))
# 	print('value:', d.get(key))


class Solution:
    def threeSum(self, nums: list) -> list:
        ans = []
        nums.sort() # O(nlgn)
        for i in range(len(nums)-2): # O(n^2)
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            left, right = i+1, len(nums)-1
            while left < right:
                Sum = nums[i] + nums[left] + nums[right]
                if Sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    if nums[left] == nums[right]:
                        break
                    left += 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                        
                    right -= 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                elif Sum > 0:
                    right -= 1
              
                else:
                    left += 1
  
        return ans

# class Solution:
# Runtime: 344 ms, faster than 98.97% of Python3 online submissions for 3Sum.
#     faster in leetcode database

#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         d = {}
#         for val in nums:
#             d[val] = d.get(val, 0) + 1
        
#         pos = [x for x in d if x > 0]
#         neg = [x for x in d if x < 0]
        
#         res = []
#         if d.get(0, 0) > 2:
#             res.append([0, 0, 0])
            
#         for x in pos:
#             for y in neg:
#                 s = -(x + y)
#                 if s in d:
#                     if s == x and d[x] > 1:
#                         res.append([y, x, x])
#                     elif s == y and d[y] > 1:
#                         res.append([y, y, x])
#                     elif y < s < x:
#                         res.append([y, s, x])
#         return res

s = Solution()
print(s.threeSum(l))        