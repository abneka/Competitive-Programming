class Solution:
    def knightDialer(self, n: int) -> int:
        direction = {0: (4, 6), 1: (8, 6), 2: (7, 9), 3: (4, 8),
                     4: (0, 3, 9), 5: (), 6: (1, 7, 0),
                     7: (2, 6), 8: (1, 3), 9: (2, 4)}
        memo = [[-1] * 10 for _ in range(n)]
        
        def dp(key, size):
            if size == 1:
                return 1
            
            if memo[size - 1][key - 1] == -1:
                option = 0
                for next_key in direction[key]:
                    option += dp(next_key, size - 1)

                memo[size - 1][key - 1] = option
            
            return memo[size - 1][key - 1]
        
        ans = 0
        modulo = (10 ** 9) + 7
        for key in range(10):
            test =dp(key, n)
            ans += test
        
        return ans % modulo