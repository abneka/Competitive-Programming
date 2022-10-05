class Solution:
    def minNonZeroProduct(self, p):
        num = 2**p -2
        nextnum = (2**p - 1)
        half = 2**(p-1) -1
        modulo = (10**9 + 7)
        mini = pow(num, half, modulo)
        return (mini * nextnum) % modulo