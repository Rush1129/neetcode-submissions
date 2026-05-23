import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        k=r
        while(l<=r):
            mid= l + (r-l)//2
            thours=0
            for i in piles:
                thours+=math.ceil(i/mid)
            if thours<=h:
                k=mid
                r=mid-1
            else:
                l=mid+1
        return k