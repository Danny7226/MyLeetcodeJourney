'''

162. Find Peak Element

Medium

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        leng = len(nums)
        if leng == 1:
            return 0
        left, right = 0, leng-1
        while left < right: # there is always a peak so we use '<' instead of '<='
            mid = (left+right) // 2
            if nums[mid] < nums[mid+1]:
                # 'left' and 'right' could be consecutive
                # 'mid' intends to be 'left', so we need 'left' to plus one to avoid endless loop			
                left = mid + 1
            else:
                right = mid
        return left