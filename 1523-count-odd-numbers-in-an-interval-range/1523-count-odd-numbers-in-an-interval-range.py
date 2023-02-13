class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if not (high - low + 1) % 2:
            return (high - low + 1) // 2
        
        else:
            if low % 2:
                return ((high - low + 1) // 2) + 1
            return ((high - low + 1) // 2)