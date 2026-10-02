class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r=1,len(nums)-2
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                r = mid-1

        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        
        return len(nums)-1