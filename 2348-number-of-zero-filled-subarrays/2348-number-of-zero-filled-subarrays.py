class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        current = 0
                
        for num in nums:
            if not num:
                current += 1
                total += current
            else:
                current = 0
                
        return total