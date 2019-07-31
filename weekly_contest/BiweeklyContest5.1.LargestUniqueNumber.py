A = [3,4,9,5,6,7,9,8,8]
import heapq
class Solution:
    # Run time O(NlogN), space O(N)
    def largestUniqueNumber(self, A: list) -> int:
        seen, double_seen = set(), set()
        pq = []
        for num in A:
            if num not in seen:
                seen.add(num)
                heapq.heappush(pq, -num)
            else:
                double_seen.add(num)
        while pq:
            res = -heapq.heappop(pq)
            if res not in double_seen:
                return res
        return -1
s = Solution()
print(s.largestUniqueNumber(A))