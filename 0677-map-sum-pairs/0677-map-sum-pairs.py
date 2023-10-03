class TrieNode:
    def __init__(self):
        self.value = 0
        self.children = defaultdict(TrieNode)

class MapSum:
    def __init__(self):
        self.map = defaultdict(int)
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        offset = 0
        if key in self.map:
            offset = self.map[key]
            
        self.map[key] = val
        curr = self.root
        for char in key:
            curr = curr.children[char]
            curr.value += val
            curr.value -= offset
        
    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return 0
        return curr.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)