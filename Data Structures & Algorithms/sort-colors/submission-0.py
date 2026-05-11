class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        counts = [0]*3

        for i in nums:
            counts[i] += 1

        index = 0

        for i in range(3):
            while(counts[i]):
                counts[i] -= 1
                nums[index] = i
                index += 1