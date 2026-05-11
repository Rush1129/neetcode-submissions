class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=''
        for c in s:
            if c.isalnum():
                ans+=c.lower()
        
        i,j=0,len(ans)-1

        while(i<len(ans) and j>=0):
            if ans[i]==ans[j]:
                i+=1
                j-=1
                continue
            return False

        return True