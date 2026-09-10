class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        per = [[nums[0]]]
        
        for i in range(1,len(nums)):
            for p in range(len(per)):
                temp = per.pop(0)
                for k in range(len(temp)+1):
                    ans = temp[:k]+[nums[i]]+temp[k:] 
                    if ans not in per:
                        per.append(ans)
        return per