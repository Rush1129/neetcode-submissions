class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        curs = -1
        for p in prices:
            if curs==-1:
                curs=p
                continue
            if p-curs>0:
                pro+=(p-curs)
            curs=p
        return pro
