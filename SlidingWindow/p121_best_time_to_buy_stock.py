class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l,r, max_profit = 0,0,0
        while r<len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            if profit < 0:
                l+=1
            else:
                r+=1
        return max_profit
