class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        pos = 0
        for char in word:
            nxt = ord(char) - ord('a')
            ans += min(abs(pos - nxt), (26 - nxt) + pos, (26 - pos) + nxt) + 1
            pos = nxt
        return ans