class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        ans = ''
        flag=False
        while n>0:
                
            temp=(n-1)%26
            ans = chr(temp+65)+ans
            n = n//26
            if flag:
                break
            if n==26:
                flag=True
            
        return ans
    