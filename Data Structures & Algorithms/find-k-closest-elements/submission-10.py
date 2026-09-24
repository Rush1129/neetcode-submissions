class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=[arr[0]]
        tmind = abs(arr[0]-x)
    
        for i in range(1,len(arr)):
            if len(l)==k:
                if abs(arr[i]-x)<tmind:
                    l.pop(0)
                    l.append(arr[i])
                    if l:
                        tmind=abs(x-l[0])
                    continue
                else:
                    continue
            l.append(arr[i])
        return l