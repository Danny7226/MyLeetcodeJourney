'''

1092. Shortest Common Supersequence

Medium

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"

Explanation: 
str1 = "abac" is a substring of "cabac" because we can delete the first "c".
str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

'''
str1, str2 = "bbbaaaba", "bbababbb"
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        ptr = 0
        output = list(str2)
        for i in range(len(str1)):
            if str1[i] in output[ptr:]:
                ptr = str2.index(str1[i]) + 1
            else:
                output.insert(ptr,str1[i])
                ptr += 1
        return ''.join(output)

s = Solution()
print(s.shortestCommonSupersequence(str1,str2))        