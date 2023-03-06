class Solution:
    def hIndex(self, citations: List[int]) -> int:
        csorted = sorted(citations, reverse=True)
        
        length = len(csorted)
        left = 0
        right = length
        
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid < length and csorted[mid] >= mid + 1:
                res = max(res, mid + 1)
                left = mid + 1
            
            else:
                right = mid -1
        
        return res
    
        
#         for i, n in enumerate(csorted):
#             if n >= i+1:
#                 res = i+1
                
#         return res