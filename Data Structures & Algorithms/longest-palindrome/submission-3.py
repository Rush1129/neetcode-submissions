class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        
        res = 0
        odd=0
        for k,v in d.items():
            if v%2==0:    
                res+=v
            else:
                res+=(v-1)
                odd=1   

        return res+odd