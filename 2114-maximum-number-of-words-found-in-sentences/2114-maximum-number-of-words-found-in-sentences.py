class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        
        for sentence in sentences:
            count = sentence.count(' ')
            maxi = max(maxi, count + 1)
            
        return maxi