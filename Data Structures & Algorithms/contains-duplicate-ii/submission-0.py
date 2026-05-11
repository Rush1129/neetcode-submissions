class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = set()
        f=nums[0]
        j=0
        for i in range(len(nums)):
            if i>k:
                f=nums[j]
                j+=1
                dup.discard(f)
            
            if nums[i] in dup:
                return True
            dup.add(nums[i])
        
        return False
    