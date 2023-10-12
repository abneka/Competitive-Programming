class Solution:
    def countOrders(self, n: int) -> int:
        memo = 1
        mod = (10 ** 9) + 7
        
        def multiply(a, b, m):
            return ((a % m) * (b % m)) % m
        
        for num in range(1, n + 1):
            num *= 2
            num = multiply(num, num -1, mod)
            num //= 2
            memo = multiply(memo, num, mod)
        
        return memo