class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nstk=[]

        for i in tokens:
            print(i,nstk)
            try:
                nstk.append(int(i))           
            except:
                a=nstk.pop()
                b=nstk.pop()
                if i=='+':
                    nstk.append(a+b)
                elif i=='-':
                    nstk.append(b-a)
                elif i=='*':
                    nstk.append(a*b)
                elif i=='/':
                    nstk.append(int(b/a))
                else:
                    nstk.append(b)
                    nstk.append(a)
            
            
        return nstk[-1]