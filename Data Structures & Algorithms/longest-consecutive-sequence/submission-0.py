class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mi,ma = 9999,0

        for i in nums:
            mi = min(i,mi)
            ma = max(i,ma)

        count = 0
        maxc = 0
        for i in range(mi,ma+1):
            if i in nums:
                count+=1
                maxc = max(maxc, count)
                continue
            count = 0

        return maxc