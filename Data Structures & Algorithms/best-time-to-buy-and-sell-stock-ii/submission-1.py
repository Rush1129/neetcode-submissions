class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # hs = dict()

        # for i in range(1,len(prices)):
        #     hs[i] = prices[i] - prices[i-1]

        # print(hs)
        # res = 0
        # for v in hs.values():
        #     if(v>0):
        #         res += v
        
        # return res

        res = 0
        for i in range(1,len(prices)):
            if(prices[i]>prices[i-1]):
                res += prices[i]-prices[i-1]
        
        return res