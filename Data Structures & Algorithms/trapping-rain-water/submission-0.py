class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = len(height)
        lmax = [0]*l
        rmax = [0]*l
        tlmax=0
        trmax=0
        for i in range(l):
            tlmax = max(tlmax,height[i])
            trmax = max(trmax,height[l-1-i])
            lmax[i] = tlmax 
            rmax[l-1-i] = trmax

        for i in range(l):
            water += min(lmax[i],rmax[i]) - height[i]

        return water