class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i!=']':
                stack.append(i) 
            else:
                t=''
                while stack and stack[-1]!='[':
                    t = stack.pop()+t
                stack.pop()

                mul=1
                num=''
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                
                stack.append(int(num)*t)
        return "".join(stack)