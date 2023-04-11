class Solution:
    def maxProduct(self, words: List[str]) -> int:
        length = [0]*len(words)
        
        for index, word in enumerate(words):
            for letter in word:
                length[index] |= (1 << (ord(letter) - 97))
        
        ans = 0
        
        for index, word1 in enumerate(length):
            for j in range(index + 1, len(words)):
                if not word1 & length[j]:
                    ans = max(ans, len(words[index]) * len(words[j]))
        return ans