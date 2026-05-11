class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = set()
  
        for i in range(len(nums)):
            if i>k:
                dup.discard(nums[i-k-1])
            
            if nums[i] in dup:
                return True
            dup.add(nums[i])
        
        return False
    