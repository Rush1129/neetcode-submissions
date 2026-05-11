class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        profit=0
        for p in range (1,len(prices)):
            profit=max(profit,prices[p]-buy)
            buy=min(buy,prices[p])

        return profit
