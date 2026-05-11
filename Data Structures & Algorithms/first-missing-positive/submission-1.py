class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        maxi = 0
  
        for i in nums:
            maxi = max(i,maxi)
            
        for i in range(1,maxi+2):
            if i not in nums:
                return i