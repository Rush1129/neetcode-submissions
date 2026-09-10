class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        pos=-1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                pos=i+1
                break
        if pos!=-1:
            snum = nums[pos:]+nums[:pos]
        else:
            snum = nums
        l,r = 0,len(snum)-1
        while l<=r:
            mid = (l+r)//2
            if snum[mid] == target:
                return True
            if snum[mid]<target:
                l = mid+1
            else:         
                r = mid-1
        
        return False