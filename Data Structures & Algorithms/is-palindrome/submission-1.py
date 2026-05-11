class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=''
        for c in s:
            if c.isalnum():
                ans+=c.lower()
        
        rs=''
        for c in range(len(ans)):
            rs+=ans[-1-c]
        
        print(ans)
        print(rs)
        if rs==ans:
            return True
        return False