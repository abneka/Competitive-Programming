class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        
        '''
        length = len(coins)
        arr = [0 for i in range(amount + 1)]
        
        for num in range(1, amount + 1):
            mini = float('inf')
            for coin in coins:
                if num - coin < 0:
                    continue
                mini = min(mini, arr[num - coin] + 1)
            
            arr[num] = mini
        
        return arr[-1] if arr[-1] != float('inf') else -1