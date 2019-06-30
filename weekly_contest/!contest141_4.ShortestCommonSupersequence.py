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
def lcs(A, B):
    n, m = len(A), len(B)
    dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + A[i]
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
    print(dp)
    return dp[-1][-1]   

print(lcs(str1,str2))