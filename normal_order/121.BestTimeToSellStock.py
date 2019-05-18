'''

tags: One Pass; Dynamic Programing

121.BestTimeToSellStock.py

Easy



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