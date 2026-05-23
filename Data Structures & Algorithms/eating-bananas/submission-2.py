import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)

        while(l<=r):
            mid=(l+r)//2
            if mid==0:
                break
            thours=0
            for i in piles:
                if(i<=mid):
                    thours+=1
                else:
                    thours+=math.ceil(i/mid)
            if thours<=h:
                k=mid
                r=mid-1
            else:
                l=mid+1
        
        return k

            
