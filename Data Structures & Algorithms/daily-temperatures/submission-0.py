class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:

        res=[0]*(len(t))
        stack=[0]

        for i in range(1,len(t)):
            if t[i]<=t[stack[-1]]:
                stack.append(i)
            else:
                while(stack != []):
                    if(t[stack[-1]]<t[i]):
                        p = stack.pop()
                        res[p]=i-p
                    else:
                        break
                stack.append(i)
        
        return res