class StockSpanner:

    def __init__(self):
        self.span = []
        

    def next(self, price: int) -> int:
        self.span.append(price)
        temp = self.span.copy()
        n=0
        while temp:
            if temp[-1]<=price:
                n+=1
                temp.pop()
            else:
                break
        return n


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)