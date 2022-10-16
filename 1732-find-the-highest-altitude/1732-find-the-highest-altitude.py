class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = total = 0
        for i in gain:
            total += i
            maxi = max(maxi, total)
            
        return maxi