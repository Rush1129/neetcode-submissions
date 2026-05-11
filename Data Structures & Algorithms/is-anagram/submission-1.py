class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
    
        for i in s:
            d[i] = d.get(i,0)+1
        
        for i in t:
            d[i] = d.get(i,0)-1

        for k,v in d.items():
            if v!=0:
                return False
        
        return True