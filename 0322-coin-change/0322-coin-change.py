class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        
        '''
        arr = [0] * (amount + 1)
        
        for index in range(1, amount + 1):
            mini = float('inf')
            for coin in coins:
                if index - coin >= 0:
                    mini = min(mini, arr[index - coin] + 1)
            arr[index] = mini
        
        return arr[-1] if arr[-1] != float('inf') else -1
                    