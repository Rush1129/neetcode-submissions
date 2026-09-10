class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        pos=-1
        nums = list(set(nums))
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                pos=i+1
                break
        if pos!=-1:
            nums = nums[pos:]+nums[:pos]

        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[mid]<target:
                l = mid+1
            else:         
                r = mid-1
        
        return False