'''

28. Implement strStr()

Easy

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

'''
haystack = "aaabacc"
needle = "bac"

class Solution:
    # str.find() returns -1 when not match
    # str.index() raises error when not match
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)

class Solution:
    '''
    The time complexity for this solution should be O(m + n). First of all, 
    we generate the "next" array to show any possible duplicates of prefix and 
    postfix within needle. Then we go through haystack. Every time we see a bad 
    match, move j to next[j] and keep i in current position; otherwise, move both 
    of them to next position.
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        i, j, m, n = -1, 0, len(haystack), len(needle)
        Next = [-1] * n
        while(j < n-1):
            if i == -1 or needle[i] == needle[j]:
                i, j = i+1, j+1
                Next[j] = i
            else:
                i = Next[i]
        print(Next)
        i, j = 0, 0
        while(i<m and j<n ):
            if j == -1 or haystack[i] == needle[j]:
                i, j = i+1, j+1
            else:
                j = Next[j]
        if j == n:
            return i-j
        return -1

s = Solution()
print(s.strStr(haystack,needle))        
