class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones)>1:
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)
            if a==b:
                continue
            heapq.heappush_max(stones, max(a,b)-min(a,b))
        
        
        return stones[0] if len(stones)==1 else 0