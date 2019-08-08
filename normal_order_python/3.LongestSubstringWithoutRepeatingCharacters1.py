'''

3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
'''
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_possible = len(set(s))
#         start = 0
#         if (len(s)==0):
#             return 0		
#         [max_so_far, start] = self.recursive(start, s, 0)
#         # print(max_so_far)
#         if (max_possible == max_so_far):
#             return max_so_far
#         while(max_so_far < (len(s) - start)):
#             [max_so_far,start] = self.recursive(start, s, max_so_far)
#         return max_so_far

#     def recursive(self, start,s:str,max_so_far):
#         tmp = {}
#         longest = 0
#         start_next = 0
#         for i in range(start,len(s)):
#             if (s[i] in tmp):
#                 longest = i - start
#                 start_next = tmp[s[i]] + 1
#                 if (longest > max_so_far):
#                     max_so_far = longest

#                 break
#             else: 
#                 tmp[s[i]] = i

#                 # print(tmp)
#         else: 
#             max_so_far = len(s) - start
#             start_next = len(s)
#         # print(start_next,tmp)
#         return [max_so_far, start_next]

a = "pwwkew"
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        sub = ''
        out = ''
        leng = 0

        for i in s:
            
            if (i in sub):
                sub = sub[sub.index(i)+1 : ] + i
            else: 
                sub += i
                
            if (leng < len(sub)):
                leng = len(sub)
                out = sub
        print(out)        
        return leng

print(Solution.lengthOfLongestSubstring(a))