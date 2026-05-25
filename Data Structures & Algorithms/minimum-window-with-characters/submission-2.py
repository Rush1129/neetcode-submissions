class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d=dict()
        ans=''
        tl=1001
        for i in t:
            d[i]=d.get(i,0)+1
        td=d
        for i in range(len(s)):
            d=td.copy()
            tt=''
            if d.get(s[i],0):
                l,r=i,i
                while(r<len(s)):
                    if d.get(s[r],0):
                        tt+=s[r]
                        d[s[r]]-=1

                    if len(tt)==len(t) and r-l<tl:
                        ans=s[l:r+1]
                        tl=r-l
                        break
                    r+=1
        return ans
