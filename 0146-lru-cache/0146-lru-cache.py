class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.hash = {}
        
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        nxt, prv = node.next, node.prev
        prv.next, nxt.prev = nxt, prv
        
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.next, node.prev = nxt, prv
    
    def get(self, key: int) -> int:
        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(self.hash[key])
            return self.hash[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])
        self.hash[key] = Node(key, value)
        self.insert(self.hash[key])
        
        if len(self.hash) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.hash[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)