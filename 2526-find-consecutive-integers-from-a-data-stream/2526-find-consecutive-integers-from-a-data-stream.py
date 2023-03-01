class DataStream:

    def __init__(self, value: int, k: int):
        self.total = value * k
        self.numbers_total = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num != self.value:
            return self.reset()
        
        if self.numbers_total + num == self.total:
            return True
        self.numbers_total += num
        return False
        
    def reset(self) -> bool:
        self.count = self.k
        self.numbers_total = 0
        
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)