class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = collections.Counter(words[0])
        
        for char in words:
            res = res & collections.Counter(char)
        return list(res.elements())