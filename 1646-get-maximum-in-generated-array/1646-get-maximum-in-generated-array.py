class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [-1] * (n + 2)
        
        def dp(num):
            if num < 2:
                return num
            if memo[num] == -1:
                half = num // 2
                if num % 2:
                    memo[num] = dp(half) + dp(half + 1)
                else:
                    memo[num] = dp(half)
            return memo[num]
        
        ans = 0
        for i in range(n):
            ans = max(ans, dp(n - i))
            
        return ans