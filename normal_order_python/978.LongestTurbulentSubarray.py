'''
978. Longest Turbulent Subarray
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
Return the length of a maximum size turbulent subarray of A.
Example 1:
Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:
Input: [4,8,12,16]
Output: 2
Example 3:
Input: [100]
Output: 1
Note:
1 <= A.length <= 40000
0 <= A[i] <= 10^9
'''
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        cp = [0] * len(A)
        for i in range(1, len(A)):
            cp[i] = 1 if A[i] > A[i-1] else -1 if A[i] < A[i-1] else 0
        print(cp)
        i, j, ans = 0, 1, 0
        while j < len(A):
            if cp[j] == 0:
                ans = max(ans, 1)
                i = j
                j += 1
                continue
            if cp[j] == -cp[j-1] or cp[j-1]==0:
                ans = max(ans, j-i+1)
                # print(i, j)
                j += 1
            else:
                i = j - 1
                j = j + 1    
        return ans