class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag=True
        cur = 0
        for i in range(1,len(nums)-1):
            if nums[i+1]<=nums[i]:
                cur = i
                break
        
        for j in range(len(nums)-1,0,-1):
            if nums[j-1]<nums[j]:
                if j==cur:
                    nums[cur-1],nums[-1] = nums[-1], nums[cur-1]
                    temp = nums[cur:]
                    temp.sort()
                    nums[cur:] = temp
                else:
                    nums[j-1],nums[j] = nums[j], nums[j-1]
                    t = nums[j:]
                    t.sort()
                    nums[j:] = t
                flag=False
                break
        if flag:
            return nums.sort()
        return nums