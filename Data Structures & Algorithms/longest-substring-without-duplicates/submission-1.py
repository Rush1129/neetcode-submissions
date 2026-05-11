class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqd=dict()
        subs=''
        maxs=0
        m=0
        for i in range(len(s)):
            if s[i] in uniqd.keys() and uniqd[s[i]]>=m:
                m=uniqd[s[i]]
                subs= s[m+1:i+1]
                uniqd[s[i]]=i
            else:
                uniqd[s[i]] = i
                subs+=s[i]
            maxs=max(maxs,len(subs))
            
        return maxs