'''

tags: backtrack

22. Generate Parentheses

Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''
n = 4
class Solution:

    def __init__(self):
        self.choice = ['(', ')']
        self.most = n
        self.output = []
    def generateParenthesis(self, n: int) -> list:
        
        if n == 0:
            return output
        if n == 1:
        	return ['()']
        else:
            self.backtrack('(',n-1)
            return self.output
        
    def backtrack(self, combination, number):
        if number == 0:
            while(len(combination) < self.most*2):
                combination += ')'
            self.output.append(combination)

        
        else:
            if combination.count('(')>combination.count(')'):
                for i in self.choice:
                    print(i)
                    if i == '(':
                        self.backtrack(combination + i, number - 1)
                    else:
                        self.backtrack(combination + i, number)
            else:
                self.backtrack(combination + '(', number - 1)

# class Solution:
#     # the same as above
#     def generateParenthesis(self, n: int) -> list:
#         choice = ['(', ')']
#         most = n
#         output = []
#         def backtrack(combination, number):
#             if number == 0:
#                 while(len(combination) < most*2):
#                     combination += ')'
#                 output.append(combination)
    
            
#             else:
#                 if combination.count('(')>combination.count(')'):
#                     for i in choice:
#                         # print(i)
#                         if i == '(':
#                             backtrack(combination + i, number - 1)
#                         else:
#                             backtrack(combination + i, number)
#                 else:
#                     backtrack(combination + '(', number - 1)

#         if n == 0:
#             return output
#         if n == 1:
#         	return ['()']
#         else:
#             backtrack('(',n-1)
#             return output
s = Solution()
print(s.generateParenthesis(n))

# x = '1231'
# print(x.count('1'))