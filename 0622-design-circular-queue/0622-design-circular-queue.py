class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.size = k
        self.left = -1
        self.right = -1
    def enQueue(self, value: int) -> bool:
        pos = (self.right + 1) % self.size
        if pos == self.left:
            return False
        self.queue[pos] = value
        self.right = pos
        if self.left == -1:
            self.left += 1
        return True
        

    def deQueue(self) -> bool:
        if self.left == -1:
            return False
        if self.left == self.right:
            self.left = -1
            self.right = -1
        else:
            self.left = (self.left + 1) % self.size
        return True

    def Front(self) -> int:
        if self.left != -1:
            return self.queue[self.left]
        return -1

    def Rear(self) -> int:
        if self.right != -1:
            return self.queue[self.right]
        return -1

    def isEmpty(self) -> bool:
        if self.left == -1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.right + 1) % self.size == self.left:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()