class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        sl = 99999
        ll = len(strs)

        if(ll==1):
            return strs[0]
        for i in range(len(strs)):
            sl = min(len(strs[i]),sl)
        i,j=0,0
        while(i<ll-1 and j<sl):
            if(strs[i][j]==strs[i+1][j]):
                i+=1
                if(i>=ll-1):
                    ans+=strs[i][j]
                    j+=1
                    i=0
                continue
            break
        
        return ans