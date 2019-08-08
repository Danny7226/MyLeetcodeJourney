'''
862. Shortest Subarray with Sum at Least K
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
If there is no non-empty subarray with sum at least K, return -1.
Example 1:
Input: A = [1], K = 1
Output: 1
Example 2:
Input: A = [1,2], K = 4
Output: -1
Example 3:
Input: A = [2,-1,2], K = 3
Output: 3
Note:
1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
'''
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        pq, Sum, asn = [(0,-1)], 0, 50001
        for i, n in enumerate(A):
            Sum += n
            while pq and Sum-K >= pq[0][0]:
                    ans = min(ans, i-heapq.heappop(pq)[1])
            heapq.heappush(pq, (Sum, i))
        return ans if ans<50001 else -1