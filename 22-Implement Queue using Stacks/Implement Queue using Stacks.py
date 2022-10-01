class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        print(self.stack)

    def pop(self) -> int:
        num = self.stack[0]
        self.stack.pop(0)
        return num

    def peek(self) -> int:
        num = self.stack[0]
        return num

    def empty(self) -> bool:
        if len(self.stack):
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
