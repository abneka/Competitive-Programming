class Solution:
    def knightDialer(self, n: int) -> int:
        direction = {0: (4, 6), 1: (8, 6), 2: (7, 9), 3: (4, 8),
                     4: (0, 3, 9), 5: (), 6: (1, 7, 0),
                     7: (2, 6), 8: (1, 3), 9: (2, 4)}
        memo = {}
        def dp(key, size):
            if size == 1:
                return 1
            
            state = (key, size)
            
            if state not in memo:
                option = 0
                for next_key in direction[key]:
                    option += dp(next_key, size - 1)

                memo[state] = option
            
            return memo[state]
        
        ans = 0
        modulo = (10 ** 9) + 7
        for key in range(10):
            test =dp(key, n)
            ans += test
        
        return ans % modulo