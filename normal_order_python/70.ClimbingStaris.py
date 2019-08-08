'''

70. Climbing Stairs

Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''
n = 60
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        i = 3
        while i <= n:
            dp[i] = dp[i-2] + dp[i-1]
            i += 1
        return dp[-1]
        
# class Solution:
# 	# backtrack
#     def climbStairs(self, n: int) -> int:
#         step = [1,2]
        
#         def backtrack(n,tmp):
#             if n == 1:
#                 tmp += '1'
#                 output.append(tmp)
#             elif n == 0:
#                 output.append(tmp)
#             else:
#                 for i in step:
#                     backtrack(n-i,tmp + str(i))
#         output = []
#         backtrack(n,'')
#         print(output)
#         return len(output)


# class Solution:
# 	# dynamic programing
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         else:
#             return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution:
	# top down dynamic programing faster with memory dict
    def __init__(self):
        self.dic = {1:1, 2:2}

    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]  

# class Solution:
# 	# bottom up dynamic program faster with memory dict
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         step = {1:1, 2:2}
#         for i in range(3,n+1):
#             step[i] = step[i-1] + step [i-2]
#         return step[n]          

s = Solution()
print(s.climbStairs(n))  
     