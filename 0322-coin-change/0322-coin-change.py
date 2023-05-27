class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        
        '''
        memo = {}
        length = len(coins)
        def dp(index, val):
            if index == length or val > amount:
                return float('inf')
            if val == amount:
                return 0
            
            state = (index, val)
            
            if not state in memo:
                take_n_repeat = dp(index, val + coins[index]) + 1
                take_n_leave = dp(index + 1, val + coins[index]) + 1
                leave = dp(index + 1, val)

                memo[state] = min([take_n_leave, take_n_repeat, leave])
                
            return memo[state]
            
            
        ans = dp(0, 0)
        
        return ans if ans != float('inf') else -1