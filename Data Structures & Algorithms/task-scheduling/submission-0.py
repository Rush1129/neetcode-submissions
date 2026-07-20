class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = {}
        for v in tasks:
            h[v] = h.get(v,0)+1
        maxh = [-v for v in h.values()]
        heapq.heapify(maxh)

        time=0
        q=deque()

        while maxh or q:
            time+=1

            if maxh:
                cnt = 1+heapq.heappop(maxh)
                if cnt:
                    q.append([cnt,time+n])
            
            if q and time==q[0][1]:
                heapq.heappush(maxh, q.popleft()[0])
            
        return time


