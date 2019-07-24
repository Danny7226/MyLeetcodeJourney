'''

tags: One Pass; Dynamic Programing

121.BestTimeToSellStock.py

Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''
class Solution:
	# one pass Dynamic Programing
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        pos = float('inf')
        max_profit = 0
        for i in prices:
            if i < pos:
                pos = i
            if (i - pos) > max_profit:
                max_profit = i - pos
        return max_profit

    # O(N)
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        L = len(prices)
        min_before = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > min_before:
                ans = max(ans, prices[i] - min_before)
            else:
                min_before = prices[i]
        return ans


    # heap, O(NlogN) 
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        before = []
        ans = 0
        heapq.heappush(before, prices[0])
        for i in range(1, len(prices)):
            if prices[i] > before[0]:
                ans = max(ans, prices[i] - before[0])
            heapq.heappush(before, prices[i])
        return ans        