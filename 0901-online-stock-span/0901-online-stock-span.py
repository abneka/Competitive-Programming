class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        while self.stack and price >= self.stack[-1][1]:
            self.stack.pop()
            
        prev_day = self.stack[-1][0] if self.stack else 0
        self.day += 1
        self.stack.append((self.day, price))
        return self.day - prev_day
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)