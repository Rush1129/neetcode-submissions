class Solution:
    def trap(self, height: List[int]) -> int:
        water,l = 0,len(height)
        lmax,rmax = [0]*l,[0]*l
        
        tlmax=trmax=0
        for i in range(l):
            tlmax = max(tlmax,height[i])
            trmax = max(trmax,height[l-1-i])
            lmax[i] = tlmax 
            rmax[l-1-i] = trmax

        for i in range(l):
            water += min(lmax[i],rmax[i]) - height[i]

        return water