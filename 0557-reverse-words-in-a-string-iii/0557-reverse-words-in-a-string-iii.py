class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        
        for index, word in enumerate(s):
            s[index] = word[::-1]
        
        return ' '.join(s)