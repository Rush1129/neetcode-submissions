class Solution:
    def simplifyPath(self, path: str) -> str:
        res = ['/']
        s=0

        while(s<len(path)):
            sflag=False   
            if len(res)==0:
                res.append('/')
            if path[s]=='/':
                if res[-1]=='/':
                    s+=1
                    continue
                res.append(path[s])
                s+=1
                continue
            if path[s]=='.' and path[s-1]=='/':
                ndot = 1
                temp = s+1
                while(temp<len(path)):
                    if path[temp] == '.':
                        ndot += 1
                        temp+=1
                    elif path[temp] != '/':
                        res.append(path[s])
                        s+=1     
                        sflag=True
                        break
                    else:
                        break
            
                if sflag:
                    continue

                if ndot==1:
                    s+=1
                if ndot==2:
                    res.pop()
                    while len(res)>0:
                        if res[-1]=='/':
                            break    
                        res.pop()
                    s+=2
                    continue

                if ndot>2:
                    res.append('.'*ndot)
                    s=temp    
                continue
            res.append(path[s])
            s+=1     

        if res[-1]=='/' and len(res)>1:
            return "".join(res[:-1])
        return "".join(res)