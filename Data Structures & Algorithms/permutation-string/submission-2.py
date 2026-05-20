class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s = {}
        for i in range(26):
            s[chr(97+i)] = 0
        
        for i in s1:
            s[i]+=1
        
        for i in range(len(s2)-len(s1)+1):
            c=0
            ts=s.copy()
            temp=s2[i:i+len(s1)]

            for j in range(len(temp)):
                if(ts[temp[j]]<=0):
                    break
                else:
                    ts[temp[j]]-=1
                    c+=1
            if c==len(s1):
                return True
        return False        
                    
            
                




        return False