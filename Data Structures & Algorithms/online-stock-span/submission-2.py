class StockSpanner:

    def __init__(self):
        self.spanstk = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day+=1
        while self.spanstk and self.spanstk[-1][1]<=price:
                self.spanstk.pop()
        span = 0 if not self.spanstk else self.spanstk[-1][0]
        self.spanstk.append((self.day, price))
        return self.day - span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)