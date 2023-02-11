class MyHashSet:

    def __init__(self):
        self.count = Counter()

    def add(self, key: int) -> None:
        self.count[key] = 1

    def remove(self, key: int) -> None:
        if not self.count[key]:
            return 
        self.count[key] = 0

    def contains(self, key: int) -> bool:
        if self.count[key]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)