class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        curs = prices[0]
        for p in range(1,len(prices)):
            if prices[p]-curs>0:
                pro+=(prices[p]-curs)
            curs=prices[p]
        return pro