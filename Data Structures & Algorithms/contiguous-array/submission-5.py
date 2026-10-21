class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n = len(nums)
        rsum=[0]
        d = {0:[-1]} 
        for i in range(len(nums)):
            if nums[i]==0:  
                rsum.append(rsum[-1]-1)
            else:
                rsum.append(rsum[-1]+1)
            if rsum[-1] not in d.keys():
                d[rsum[-1]] = [i]
            else:
                d[rsum[-1]].append(i)

        if rsum[-1]==0:
            return n
        res = 0
        for v in d.values():
            res = max(res, v[-1]-v[0]) 

        print(rsum)
        return res