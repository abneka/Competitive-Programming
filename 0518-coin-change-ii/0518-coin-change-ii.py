class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [1] + ([0] * amount)
        inbound = lambda col : 0 <= col < amount + 1
        
        for coin in coins:
            for col in range(1, amount + 1):
                if inbound(col - coin):
                    memo[col] += memo[col - coin]
        
        return memo[-1]