class Solution:    
    def maxProfit(self, prices: List[int]) -> int:
        buyIndex = 0 # first day
        sellIndex = 1 # second day
        maxProfit = 0
        while sellIndex < len(prices):
            if prices[buyIndex] < prices[sellIndex]:
                profit = prices[sellIndex] - prices[buyIndex]
                maxProfit = max(profit, maxProfit)
            else:
                buyIndex = sellIndex
            sellIndex += 1
        return maxProfit