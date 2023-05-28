class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        length = len(coins)
        memo = [[-1] * amount for _ in range(length)]
        def dp(index, val):
            if val == amount:
                return 1
            
            if index == length or val > amount:
                return 0
            
            if memo[index][val] == -1:
                memo[index][val] = dp(index, val + coins[index]) + dp(index + 1, val)
            
            return memo[index][val]
        
        return dp(0, 0)