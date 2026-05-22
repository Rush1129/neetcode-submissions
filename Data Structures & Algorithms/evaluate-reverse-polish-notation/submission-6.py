class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nstk=[]
        op = {'+','-','*','/'}
        for i in tokens:
            if i not in op:
                nstk.append(int(i))           
            else:
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