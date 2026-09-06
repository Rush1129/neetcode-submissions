class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('inf')
        l=0
        flag = False
        curs=0
        for r in range(len(nums)):
            curs += nums[r]
            while curs>=target:
                res = min(res, r-l+1)
                curs-=nums[l]
                l+=1
                flag=True
        if not flag:
            return 0
        return res