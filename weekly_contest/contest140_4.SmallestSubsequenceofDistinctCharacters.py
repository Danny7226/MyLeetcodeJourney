'''

Smallest Subsequence of Distinct Characters

Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

Example 1:
Input: "cdadabcc"
Output: "adbc"

Example 2:
Input: "abcd"
Output: "abcd"

Example 3:
Input: "ecbacba"
Output: "eacb"

Example 4:
Input: "leetcode"
Output: "letcod"

'''
text = "cdadabcc"

# class Solution:
#     def smallestSubsequence(self, text: str) -> str:
#         last = {c: i for i, c in enumerate(text)}
#         print(last)
#         res = ""
#         left = 0
#         while last:
#             right = min(last.values())
#             c, i = min((text[i], i) for i in range(left, right + 1) if text[i] not in res)
#             left = i + 1
#             res += c
#             del last[c]
#         return res        
        

class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        last_idx = dict()
        for i, c in enumerate(text):
            last_idx[c] = i
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue
            while stack and c < stack[-1] and last_idx[stack[-1]] > i:
                stack.pop()
            stack.append(c)
            print(stack)
        return ''.join(stack)

s = Solution()
print(s.smallestSubsequence(text))  
a = ('e',1)
b = ('a',2)
print(min(a,b))      