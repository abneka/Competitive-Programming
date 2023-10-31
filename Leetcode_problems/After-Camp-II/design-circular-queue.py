class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.left = -1
        self.right = -1
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.right = (self.right + 1) % self.k
        if self.left == -1:
            self.left = self.right
        self.queue[self.right] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.left == self.right:
            self.left = -1
            self.right = -1
            return True
        self.left = (self.left + 1) % self.k
        return True

    def Front(self) -> int:
        return self.queue[self.left]

    def Rear(self) -> int:
        return self.queue[self.right]

    def isEmpty(self) -> bool:
        return self.right == -1 and self.left == -1

    def isFull(self) -> bool:
        return (self.right + 1) % self.k == self.left


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()