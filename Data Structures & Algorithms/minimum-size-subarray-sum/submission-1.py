class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('inf')
        l=0
        flag = False
        for r in range(len(nums)):
            curs = sum(nums[l:r+1])
            while curs>=target:
                res = min(res, r-l+1)
                curs-=nums[l]
                l+=1
                flag=True
        if not flag:
            return 0
        return res