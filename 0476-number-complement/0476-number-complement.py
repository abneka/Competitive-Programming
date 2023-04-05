class Solution:
    def findComplement(self, num: int) -> int:
        shift = 1
        
        while num >= shift:
            shift <<= 1
        
        return (shift - 1) - num