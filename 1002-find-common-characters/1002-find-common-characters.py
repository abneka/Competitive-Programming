class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = collections.Counter(words[0])
        
        for word in words:
            counter = counter & collections.Counter(word)
        
        counter = list(counter.elements())
        
        return counter