'''

189. Rotate Array

Easy

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

'''
k = 3
a = [1,2,3,4,5,6,7]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(num, left, right):
            right = right - 1
            while(left < right):
                tmp = num[left]
                num[left] = num[right]
                num[right] = tmp
                left += 1
                right -= 1
            return
        k = k % len(nums)
        # nums[1:len(nums)] is a new list stored in a new place, thus not an in-place manipulation
        reverse(nums,0,len(nums))
        reverse(nums, 0, k)
        reverse(nums,k, len(nums))