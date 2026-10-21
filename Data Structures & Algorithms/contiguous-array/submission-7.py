class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n = len(nums)
        bal=0
        d = {0:-1} 
        res=0
        for i in range(len(nums)):
            if nums[i]==0:  
                bal-=1
            else:
                bal+=1

            if bal not in d.keys():
                d[bal] = i
            else:
                res = max(res, i-d[bal]) 

        return res