class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mini or x <= self.mini[-1]:
            self.mini.append(x)
            

    def pop(self) -> int:
        if self.stack:
            if self.stack[-1] == self.mini[-1]:
                self.mini.pop()
            return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.mini[-1]


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()