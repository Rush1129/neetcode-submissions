class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = len(nums),0
        i=1
        pre = nums[0]

        while i<l:
            if pre==nums[i-r]:
                nums.pop(i-r)
                r+=1
            else:
                pre=nums[i-r]
            i+=1

        return i-r