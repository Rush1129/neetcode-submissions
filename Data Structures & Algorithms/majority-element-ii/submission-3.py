class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        
        for n in nums:
            count[n] = count.get(n,0)+1

        ans=[]
        for k,v in count.items():
            if v>(len(nums)//3):
                ans.append(k)
        
        return ans