class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxe=1
        mine=1
        hs=nums[0]

        for i in nums:

            m= maxe*i

            maxe = max(i*maxe,i*mine,i) 
            mine = min(m,mine*i,i)
            
            hs = max(hs,maxe)
        
        return hs