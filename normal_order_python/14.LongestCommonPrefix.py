'''

tag: string

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''

strs = ["flower","fow","flight"]

# class Solution:
#     def longestCommonPrefix(strs: list) -> str:
        
#         def findCommon(a:str, b:str):

#             print(a,b)
#             output = ''
#             leng = min(len(a), len(b))
#             if leng == 0:
#                 return output

#             for i in range(leng,-1,-1):
#                 print(i)
#                 if(a[:i] == b[:i]):
#                     return a[:i]
#                 else:
#                     continue
#             else: 
#                 return output
                
#         output = ''
#         if len(strs) == 0:
#             return output
#         if len(strs) == 1:
#             return strs[0]
#         output = findCommon(strs[0], strs[1])
#         print(output)
#         for i in range(2, len(strs)):
#             output = findCommon(output, strs[i])
#         return output
            
class Solution:
    def longestCommonPrefix(strs: 'List[str]') -> 'str':
        prefix = ''
        if not strs: return prefix
        strs.sort()
        print(strs)
        first = strs[0]
        last = strs[-1]
        '''
        strs.sort() and compare between strs[0] and strs[-1] are 
        the tricks of this solution

        '''

        for ch1,ch2 in zip(first,last):
            if ch1 == ch2:
                prefix += ch1
            else:
                break
        return prefix


print(Solution.longestCommonPrefix(strs))        
# print(list(zip(strs[0], strs[1])))        