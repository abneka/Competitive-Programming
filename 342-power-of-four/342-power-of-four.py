class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while (n % 4) == 0 and n != 0:
            n /= 4
            
        return True if n == 1 else False