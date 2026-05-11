class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        j = n-1
        fstr, rstr = '',''
        for i in range(n):
            if(s[i].isalnum()):
                fstr += s[i].lower()
            
            if(s[j].isalnum()):
                rstr += s[j].lower()
            j-=1

        if fstr==rstr:
            return True
        
        return False