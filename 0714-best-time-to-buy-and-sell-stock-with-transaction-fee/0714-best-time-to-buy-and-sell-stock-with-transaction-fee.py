class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        memo = [[-1] * 2 for _ in range(length)]
        def dp(index, isBuyer):
            if index == length:
                return 0
            
            state = (index, isBuyer)
            
            if memo[index][isBuyer] == -1:
                
                if isBuyer:
                    buy_now = dp(index + 1, 0) - prices[index]
                    buy_later = dp(index + 1, 1)
                    memo[index][isBuyer] = max(buy_now, buy_later)
                
                else:
                    sell_now = dp(index + 1, 1) + prices[index] - fee
                    sell_later = dp(index + 1, 0)
                    memo[index][isBuyer] = max(sell_now, sell_later)
            
            return memo[index][isBuyer]
        
        return dp(0, 1)
            