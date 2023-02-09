class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            checker = set()
            checker.add(word)
            checker.add(word[::-1])
            
            if len(checker) == 1:
                return word
        
        return ''