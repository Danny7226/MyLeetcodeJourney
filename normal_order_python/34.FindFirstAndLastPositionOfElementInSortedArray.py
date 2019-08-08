'''

tags: Binary Array

34. Find First and Last Position of Element in Sorted Array

Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''

nums, target = [5,7,7,8,8,10], 8

class Solution:
    def searchRange(self, nums: list, target: int) -> list:
            lo = 0
            hi = len(nums) - 1
            ptr1 = ptr2 = -1
            while (lo <= hi):
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    ptr1 = ptr2 = mid
                    i = 1
                    while mid+i<len(nums) and nums[mid+i] == target:
                        ptr2 = mid + i 
                        i += 1 
                    i = 1
                    while mid-i>=0 and nums[mid-i] == target:
                        ptr1 = mid - i
                        i += 1
                    break
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return [ptr1, ptr2]

# class Solution:
#     def searchRange(self, nums, target):
#         def binarySearchLeft(A, x):
#             left, right = 0, len(A) - 1
#             while left <= right:
#                 mid = (left + right) / 2
#                 if x > A[mid]: left = mid + 1
#                 else: right = mid - 1
#             return left

#         def binarySearchRight(A, x):
#             left, right = 0, len(A) - 1
#             while left <= right:
#                 mid = (left + right) / 2
#                 if x >= A[mid]: left = mid + 1
#                 else: right = mid - 1
#             return right
            
#         left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
#         return (left, right) if left <= right else [-1, -1]            

s = Solution()
print(s.searchRange(nums, target))            