class MinStack:

    def __init__(self):
        self.stack = []
        self.minh = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minh or val < self.minh[-1]:
            self.minh.append(val)
        else:
            self.minh.append(self.minh[-1])
            
    def pop(self) -> None:
        p = self.stack.pop()
        self.minh.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minh[-1]