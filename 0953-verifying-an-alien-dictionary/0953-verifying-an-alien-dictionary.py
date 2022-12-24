class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {char : index for index, char in enumerate(order)}
        
        words = [[order[c] for c in w] for w in words]
        # print(order)
        # words.sort()
        # print(words)
        return all(words[i] <= words[i+1] for i in range(len(words) - 1))