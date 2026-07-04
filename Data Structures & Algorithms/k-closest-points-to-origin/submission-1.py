class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]

        for p in points:
            heapq.heappush(res,[-(p[0]**2 + p[1]**2),p])
            if len(res)>k:
                heapq.heappop(res)

        return [r[1] for r in res]