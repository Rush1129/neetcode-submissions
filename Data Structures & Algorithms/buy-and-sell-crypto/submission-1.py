class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = prices[0], 0
        profit=0
        for p in prices:
            if p>buy:
                sell=p-buy
                profit=max(profit,sell)
            else:
                buy=p

        return profit
