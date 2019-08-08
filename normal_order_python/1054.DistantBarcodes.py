'''
1054. Distant Barcodes
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.
Example 1:
Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:
Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
Note:
1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
'''
class Solution:
    def rearrangeBarcodes(self, barcodes):
        count, pq, ans = {}, [], []
        for num in barcodes:
            try: 
                count[num] += 1
            except:
                count[num] = 1
        for n, c in count.items():
            heapq.heappush(pq, (-c, n))
        prev_cnt, prev_num = 0, 0
        while pq:
            cnt, num = heapq.heappop(pq)
            if prev_cnt:
                heapq.heappush(pq, (prev_cnt, prev_num))
            ans.append(num)
            prev_cnt, prev_num = cnt+1, num
        return ans