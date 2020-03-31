'''

tags: Greedy

122. Best Time to Buy and Sell Stock II

Easy

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''

prices = [2,1,2,1,0,0,1]

class Solution:
    def maxProfit(self, prices: list) -> int:
        profit = 0
        if len(prices) <= 1:
            return profit
        low = prices[0]
        # solution 1
        # for i in range(1, len(prices)):
        #     if i < len(prices)-1 and prices[i-1] >= prices[i] and prices[i] < prices[i+1]:
        #         print('1:',i)
        #         low = prices[i]
        #     elif prices[i-1] < prices[i]:
        #         if i == len(prices) -1:
        #             print('2.1:',i, end = '')
        #             profit += prices[-1] - low
        #             print('  profit:',profit)                
        #         elif prices[i] >= prices[i+1]:
        #             print('2.2:',i, end = '')
        #             peak = prices[i]
        #             profit += peak - low
        #             print('  profit:',profit)   

        # solution 2
        # This solution follows the logic used in Approach 2 itself, but with only a slight 
        # variation. In this case, instead of looking for every peak following a valley, we
        # can simply go on crawling over the slope and keep on adding the profit obtained from
        # every consecutive transaction. In the end,we will be using the peaks and valleys 
        # effectively, but we need not track the costs corresponding to the peaks and valleys along
        # with the maximum profit, but we can directly keep on adding the difference between the
        # consecutive numbers of the array if the second number is larger than the first one, and
        # at the total sum we obtain will be the maximum profit.        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]                           
        return profit

s = Solution()
print(s.maxProfit(prices))        