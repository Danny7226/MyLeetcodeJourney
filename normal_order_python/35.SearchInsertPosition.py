'''

tags: binary search

35. Search Insert Position

Easy

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

'''

# class Solution:
#	  # 1 ptr
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         else:
#             ptr = len(nums)-1
#             while(ptr>=0):
#                 if target < nums[ptr]:
#                     ptr -= 1
#                 else:
#                     return ptr + 1
#             return 0
nums = [1,3,5,6]
target = 7

class Solution:
	# binary search
    def searchInsert(self, nums: list, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            low = 0
            high = len(nums) - 1
            pos = 0
            while(low <= high):
                mid = low + (high - low)//2
                print(mid)
                if target > nums[mid]:
                    low = mid + 1
                    pos = mid + 1
                    print('pos1:',pos)
                else:
                    high = mid - 1
                    pos = mid
                    print('pos2:',pos)
            return pos

s = Solution()
print(s.searchInsert(nums,target))