class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [-1] * k
        self.r, self.f = 0, 0
        self.size = 0
        self.dequeSize = k
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.deque[self.f] = value
        else:
            self.f = (self.f-1) % self.dequeSize
            self.deque[self.f] = value
        self.size += 1
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.deque[self.r] = value
        else:
            self.r = (self.r+1) % self.dequeSize
            self.deque[self.r] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        elif self.f == self.r:
            self.deque[self.f] = -1
        else:
            self.deque[self.f] = -1
            self.f = (self.f+1) % self.dequeSize
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        elif self.f == self.r:
            self.deque[self.f] = -1
        else:
            self.deque[self.r] = -1
            self.r = (self.r-1) % self.dequeSize
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.deque[self.f]

    def getRear(self) -> int:
        return self.deque[self.r]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.dequeSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
