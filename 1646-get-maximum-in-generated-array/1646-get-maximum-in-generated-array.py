class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [-1] * (n + 2)
        if not n:
            return 0
        
        def getMax(n) :
            if n <= 1:
                return n
            if memo[n] == -1:
                half = n // 2
                if n % 2:
                    memo[n] = max(memo[n], getMax(half) + getMax(half + 1))
                else:
                    memo[n] = max(memo[n], getMax(half))
            return memo[n]
        
        ans = 0
        for i in range(n):
            ans = max(ans, getMax(n - i))
        return ans