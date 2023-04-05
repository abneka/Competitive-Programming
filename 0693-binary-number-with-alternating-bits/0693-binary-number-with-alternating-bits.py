class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bitFlag = n & 1

        while n:
            if  n & 1 != bitFlag:
                return False
            
            bitFlag ^= 1
            n >>= 1
            
        return True