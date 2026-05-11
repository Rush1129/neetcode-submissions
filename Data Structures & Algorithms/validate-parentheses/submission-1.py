class Solution:
    def isValid(self, s: str) -> bool:
        l = list()
        for i in s:
            l.append(i)
            print(len(l))
            if len(l)>=2:
                if (l[-1]==')' and l[-2]=='(') or (l[-1]=='}' and l[-2]=='{') or (l[-1]==']' and l[-2]=='['):
                    l.pop()
                    l.pop()
        
        if l==[]:
            return True
        else:
            return False