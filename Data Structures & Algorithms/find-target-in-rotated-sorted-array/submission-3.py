class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<r:
            m=(l+r)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1 
        
        nnums = nums[l:]+nums[:l]
        minl = l
        l,r=0,len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nnums[mid]==target:
                return (minl+mid)%len(nums)
            
            if nnums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        
        return -1