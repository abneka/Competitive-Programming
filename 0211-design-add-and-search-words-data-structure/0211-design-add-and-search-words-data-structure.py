class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str, curr = None) -> bool:
        if not curr:
            curr = self.root
        for index, char in enumerate(word):
            if char == '.':
                for ch in curr.children:
                    if self.search(word[index + 1:], curr.children[ch]):
                        return True
                return False
            
            else:
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    return False
        
        return curr.isWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)