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
l = [-1, 0, 1, 2, -1, -4]

d = {'a':1, 'b':2}
for i, key in enumerate(d):
	print(i,key, end = '    {0}.'.format(key))
	print('value:', d.get(key))


class Solution:
# Runtime: 792 ms, faster than 80.68% of Python3 online submissions for 3Sum.
    def threeSum(nums: list) -> list:
        nums.sort()
        output = []
        # print(nums)

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                # print(1)
                continue
            minsum = nums[i] + nums[i+1] + nums[i+2]
            maxsum = nums[i] + nums[-1] + nums[-2]
            if(minsum > 0):
                return output
            if(maxsum < 0):
                continue
            
            
            l = i+1
            r = len(nums) - 1
            while(l < r):
                thsum = nums[i] + nums[l] + nums[r]
                if thsum < 0 :
                    l += 1
                elif thsum > 0:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        return output

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

print(Solution.threeSum(l))        