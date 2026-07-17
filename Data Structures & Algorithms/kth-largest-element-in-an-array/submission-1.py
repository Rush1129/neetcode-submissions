class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]

        heapq.heapify(h)
        
        for n in range(k,len(nums)):
            heapq.heappush(h,nums[n])

            if len(h)>k:
                heapq.heappop(h)
        
        return h[0]
