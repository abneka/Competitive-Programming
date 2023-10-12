class Solution:
    def countOrders(self, n: int) -> int:
        memo = 1
        mod = (10 ** 9) + 7
        
        for num in range(1, n + 1):
            num *= 2
            memo *= (num * (num - 1)//2)
        
        return memo % mod