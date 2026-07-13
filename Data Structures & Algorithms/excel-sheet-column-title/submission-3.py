class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        ans = ''
        while n>0:
            n-=1     
            ans = chr((n%26)+65)+ans    
            n = n//26
        return ans