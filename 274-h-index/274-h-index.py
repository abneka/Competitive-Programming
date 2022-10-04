class Solution:
    def hIndex(self, citations: List[int]) -> int:
        csorted = sorted(citations, reverse=True)
        res = 0
        
        for i, n in enumerate(csorted):
            if n >= i+1:
                res = i+1
                
        return res