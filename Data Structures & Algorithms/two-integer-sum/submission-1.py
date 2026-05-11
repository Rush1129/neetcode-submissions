class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i in range(len(nums)):
            inv = target - nums[i]
            if nums[i] in d.keys():
                return [d[nums[i]],i]
            d[inv]=i
