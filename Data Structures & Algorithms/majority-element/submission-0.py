class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        d = dict()

        for i in nums:
            d[i] = d.get(i,0) + 1

        maxk = nums[0]
        maxv = d[maxk]
        for k,v in d.items():
            tmaxv = maxv
            maxv = max(maxv, v)
            if(tmaxv != maxv):
                maxk = k
        
        return maxk