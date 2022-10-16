class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = float('-inf')
        total = 0
        for i in gain:
            total += i
            maxi = max(maxi, total)
            
        return maxi if maxi > 0 else 0