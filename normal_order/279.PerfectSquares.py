'''
tags: DP
279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
class Solution(object):
    _dp = [0] # static matters, it is faster and efficient when doing multiple test cases
    def numSquares(self, n):
        dp = self._dp
        while len(dp)<=n:
            dp += [min(dp[-c*c] for c in range(1, int(len(dp)**0.5+1))) + 1]
            # print(dp)
        return dp[n]
    