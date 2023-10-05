class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.length = 0
        self.end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key = lambda word: len(word))
        root = TrieNode()
        result = ''
        size = 0
        for word in words:
            curr = root
            length = len(word)
            for char in word:
                index = ord(char) - ord('a')
                if not curr.children[index]:
                    if (not curr.length and length == 1) or curr.length == length - 1:
                        curr.children[index] = TrieNode()
                        curr.children[index].length = curr.length + 1
                        if size == curr.length + 1:
                            result = min(result, word)
                        else:
                            size = curr.length + 1
                            result = word
                    else:
                        break
                curr = curr.children[index]
        return result