class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            inv = target - nums[i]
            if(inv in d.keys()):
                return [d[inv],i]

            d[nums[i]] = i