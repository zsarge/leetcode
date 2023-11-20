class Solution:    
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        
        for price in prices:
            min_price = min(price, min_price) # left sliding window
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit) # right (selective) sliding window
            
        return max_profit