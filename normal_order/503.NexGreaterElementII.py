'''

503. Next Greater Element II

Medium

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

'''
class Solution:
    # stack
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        ans = [-1] * leng
        stack, i = [], leng - 1
        for _ in range(2*len(nums)):
            cur = nums[i]
            while stack and stack[-1] <= cur:
                stack.pop()            
            if stack:
                ans[i] = stack[-1]
            stack.append(cur)
            i -= 1
            if i == -1:
                i = leng-1
        return ans