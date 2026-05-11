class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i,0) + 1

        # arr=[]
        # for key, val in d.items():
        #     arr.append([val,key])
        # arr.sort()

        # res = []
        # for i in range(k):
        #     res.append(arr.pop()[1])
        
        # return res

        d = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            d[i] = d.get(i,0) + 1

        for key, val in d.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if(len(res) == k):
                    return res

        