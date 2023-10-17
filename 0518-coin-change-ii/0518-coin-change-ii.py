class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        length = len(coins)
        @cache
        def dp(index, total):
            if index == length or total > amount:
                return 0
            
            if total == amount:
                return 1
            
            return dp(index + 1, total) + dp(index, total + coins[index])
            
        return dp(0, 0)