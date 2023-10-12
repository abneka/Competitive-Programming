class Solution:
    def countOrders(self, n: int) -> int:
        memo = [-1] * (n + 1)
        mod = (10 ** 9) + 7
        
        def dp(n):
            if n == 1:
                return 1
            num = 2 * n
            if memo[n] == -1:
                memo[n] = dp(n - 1) * ((num * (num -1))//2)
            return memo[n]
        
        return dp(n) % mod