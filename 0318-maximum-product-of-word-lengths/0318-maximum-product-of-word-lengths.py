class Solution:
    def maxProduct(self, words: List[str]) -> int:
        length = [0]*len(words)
        
        for i in range(len(words)):
            for l in words[i]:
                length[i] |= (1 << (ord(l) - 97))
        
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if length[i] & length[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans