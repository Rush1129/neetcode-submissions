class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = mean*(len(rolls)+n)-sum(rolls)
        
        if s<n or s>n*6:
            return []

        ans=[]
        i=1
        while s>0 and i<=n:
            if s-n+i-6>=0:
                ans.append(6)
                s -= 6
                i+=1
            else:
                ans.append(s-n+i)
                i+=1
                break
        if i<=n:
            ans.extend([1]*(n-i+1))
        return ans