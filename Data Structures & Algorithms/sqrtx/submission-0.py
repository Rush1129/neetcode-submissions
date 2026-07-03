class Solution:
    def mySqrt(self, x: int) -> int:
        diff=float('inf')
        ans=0
        l,r=0,x

        while(l<=r):
            mid=(l+r)//2
            sq=mid**2
            if sq==x:
                return mid
            elif diff>sq-x and sq-x>0:
                diff=sq-x
                ans=mid
            elif sq>x:
                r=mid-1
            else:
                l=mid+1
        
        return ans-1
