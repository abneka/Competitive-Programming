class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = [ord(i) for i in s]
        t = [ord(i) for i in t]
        return chr(sum(t)-sum(s))