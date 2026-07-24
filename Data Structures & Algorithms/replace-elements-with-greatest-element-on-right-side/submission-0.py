class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l=-1
        for i in range(len(arr)-2,-1,-1):
            m=arr[i]
            arr[i] = max(arr[i+1], l)
            l=m
        arr[-1] = -1
        return arr