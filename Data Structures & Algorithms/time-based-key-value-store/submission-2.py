class TimeMap:
    def __init__(self):
        self.timedict = dict()
        self.s=set()
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.s:
            self.timedict[key]=[]
        self.timedict[key].append([timestamp,value])
        self.s.add(key)

    def get(self, key: str, timestamp: int) -> str:
        if not self.timedict.get(key):
            return ""
    
        l=0
        ans=""
        getlist = self.timedict[key]
        r=len(getlist)-1
        while(l<r):
            mid=(l+r+1)//2
            if getlist[mid][0]>timestamp:
                r=mid-1
            else:
                l=mid
            
        if getlist and getlist[l][0] <= timestamp:
            return getlist[l][1]
        return ''
            