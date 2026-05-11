class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1

        arr=[]
        for key, val in d.items():
            arr.append([val,key])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        
        return res