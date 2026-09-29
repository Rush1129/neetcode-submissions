class Solution:
    def decodeString(self, s: str) -> str:
        def ds(subs):
            ss=0
            t=''
            while ss<len(subs):
                n=ss
                num=''
                while subs[n].isdigit():
                    num+=subs[n]
                    n+=1
                if num:
                    ss=n-1
                    k = int(num)
                    ret = ds(subs[ss+1:])
                    t += k*ret[0]
                    ss += ret[1]+1
                    continue
                elif subs[ss] == ']':
                    return [t,ss+1]
                elif subs[ss] != '[':
                    t+=subs[ss]
                ss+=1
            return [t,ss]
        return ds(s)[0]

