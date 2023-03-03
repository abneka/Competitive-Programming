class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        res = right
        
        while left <= right:
            k = (left + right) // 2
            
            total = 0
            
            for pile in piles:
                total += math.ceil(pile / k)
            
            if total <= h:
                res = min(res, k)
                right = k - 1
            
            else:
                left = k + 1
        
        return res