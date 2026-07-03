class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1: return 1
        ans=0
        l,r=0,x//2

        while(l<=r):
            mid=(l+r)//2
            sq=mid**2
            if sq==x:
                return mid
            elif sq>x:
                r=mid-1
            else:
                ans=mid
                l=mid+1
        
        return ans
