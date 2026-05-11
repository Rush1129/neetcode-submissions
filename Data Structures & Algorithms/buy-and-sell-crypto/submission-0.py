class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices)==0:
            return 0

        buy, sell = prices[0], 0
        profit=0
        for p in prices:
            if p>buy:
                sell=p-buy
                profit=max(profit,sell)
            else:
                buy=p
                
        return profit
