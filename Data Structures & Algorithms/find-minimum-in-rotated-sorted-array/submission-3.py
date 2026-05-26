class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<3:
            if len(nums)==1:
                return nums[0]
            elif len(nums)==2:
                return nums[0] if nums[0]<nums[1] else nums[1]

        if nums[0]<nums[1] and nums[0]<nums[-1]:
            return nums[0]
        elif nums[-1]<nums[0] and nums[-2]>nums[-1]:
            return nums[-1]
        
        l,r=1,len(nums)-2

        while(l<=r):
            mid=(l+r)//2
            if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                return nums[mid]
            if nums[mid]>nums[mid+1]:
                if nums[mid+1]<nums[mid+2]:
                    return nums[mid+1]

            if nums[mid]<nums[r]:
                r=mid-1
            else:
                l=mid+1
            
