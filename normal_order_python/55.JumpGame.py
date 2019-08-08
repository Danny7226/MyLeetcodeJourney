'''

tags: Greedy

55. Jump Game

Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

'''

nums = [0,2,3]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        L = len(nums)
        j = L - 1
        i = j - 1
        while i >= 0:
            if i + nums[i] >= j:
                j = i
            i = i - 1
        return j == 0
        
class Solution:
    # very fast, Greedy O(n)
    def canJump(self, nums: list) -> bool:
        lastpos = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            # print(i, nums[i],lastpos)
            if i + nums[i] >= lastpos:
                lastpos = i
        return lastpos == 0
# class Solution:
#     # very slow O(n^2)
#     def canJump(self, nums: list) -> bool:
#         N = len(nums)
#         ans = [False] * N
#         ans[0] = True
#         for i in range(N-1):
#             if ans[i]:
#                 Max = min(N, i+nums[i])
#                 for j in range(1, Max+1):
#                     if i+j < N:
#                         ans[i+j] = True
#         print(ans)
#         return ans[-1]

s = Solution()
print(s.canJump(nums))        