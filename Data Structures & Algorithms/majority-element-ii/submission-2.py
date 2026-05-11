class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hs = defaultdict(int)

        for i in nums:
            hs[i] += 1

        res = []
        for k,v in hs.items():
            if(v>len(nums)//3):
                res.append(k)
        
        return res