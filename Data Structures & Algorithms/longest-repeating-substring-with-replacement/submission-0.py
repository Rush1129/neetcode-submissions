from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)

        l,r=0,0
        maxv=0
        res=0
        while(l<=r and r<len(s)):
            d[s[r]]+=1
    
            for key,v in d.items():
                if v>maxv:
                    maxv=v

            if (r-l+1)-maxv<=k:
                res=max(res, r-l+1)
                r+=1
            else:
                d[s[l]]-=1
                d[s[r]]-=1
                l+=1

        return res