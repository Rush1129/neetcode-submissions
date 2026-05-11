class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=0
        d = dict()
        
        if len(nums)==0:
            return 0

        for i in nums:
            if i-1 not in nums:
                d[i]={i}
        print(d)
        lcs=1
        for k in d.keys():
            ccs=1
            next=k+1
            while True:
                if next in nums:
                    ccs+=1
                    next+=1
                else:
                    break

            lcs=max(lcs,ccs)
        return lcs