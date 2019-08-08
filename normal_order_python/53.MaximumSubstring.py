'''

tags: Dynamic Programing

53. Maximum Subarray

Easy 

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''
nums = [-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = - float('inf')
        tmp = 0
        for i in nums:
            tmp += i
            ans = max(ans, tmp)
            if tmp < 0:
                tmp = 0
        return ans
    
    def maxSubArray(self, nums: list) -> int:
        ptr1 = 0
        ptr2 = 0
        tmp = 0
        Max = nums[0]
        for i in range(len(nums)):
            tmp += nums[i]
            print('tmp:',tmp,'max:',Max)
            if tmp > Max:
                # print('change ptr2')
                Max = tmp

                # print(ptr2)
                output = nums[ptr1:i+1]
                start = ptr1 
                end = i
            if tmp < 0:
                tmp = 0
                ptr1 = i+1
          
        print(start, end, output)
        return Max

s = Solution()
print(s.maxSubArray(nums))            