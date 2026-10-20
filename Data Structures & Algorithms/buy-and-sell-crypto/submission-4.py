class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpr = prices[0]
        maxpt = 0
        for i in range(len(prices)):
            if minpr>prices[i]:
                minpr = prices[i]
            maxpt = max(maxpt, prices[i]-minpr)
        return maxpt