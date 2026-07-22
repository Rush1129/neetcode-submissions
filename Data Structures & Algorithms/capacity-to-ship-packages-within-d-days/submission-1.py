class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=mw = max(weights)
        r=sw = sum(weights)
        ans=r
        while l<=r:
            mid = (l+r)//2
            cnt=1
            s=0
            for i in weights:
                if s+i>mid:
                    cnt+=1
                    s=0
                s+=i
                    
            if cnt<=days:
                ans = min(ans,mid)
                r=mid-1 
            else:
                l=mid+1
            
        return ans