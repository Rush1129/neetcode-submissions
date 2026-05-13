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
        if self.timedict[key]==None:
            return ""
        else:
            l=0
            ans=""
            getlist = self.timedict[key]
            r=len(getlist)-1
            while(l<=r):
                if getlist[l][0]==timestamp:
                    return getlist[l][1]
                elif getlist[l][0]<timestamp:
                    ans = getlist[l][1]
                    l+=1
                elif getlist[r][0]>timestamp:
                    r-=1
            return ans
            