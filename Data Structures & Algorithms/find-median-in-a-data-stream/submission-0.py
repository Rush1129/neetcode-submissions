class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(s, num: int) -> None:
        heapq.heappush(s.small, -1*num)

        if (s.small and s.large and -1*s.small[0]>s.large[0]):
            val = heapq.heappop(s.small)
            heapq.heappush(s.large, -1*val)

        if len(s.small)>len(s.large)+1:
            val = -1*heapq.heappop(s.small)
            heapq.heappush(s.large, val)
        if len(s.large)>len(s.small)+1:
            val = heapq.heappop(s.large)
            heapq.heappush(s.small, -1*val)

    def findMedian(s) -> float:
        if len(s.small)>len(s.large):
            return -1*s.small[0]        
        if len(s.large)>len(s.small):
            return s.large[0]

        return (-1*s.small[0] + s.large[0] ) / 2
