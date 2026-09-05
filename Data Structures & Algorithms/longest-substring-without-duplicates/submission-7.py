class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        cur = s[0]
        h = {s[0]:0}
        res=1
        t=-1
        for i in range(1,len(s)):
            if s[i] in h.keys() and h[s[i]]>t:
                cur = s[h[s[i]]+1:i]
                t=h[s[i]]
            h[s[i]]=i
            cur += s[i]
            res = max(res, len(cur))
        
        return res