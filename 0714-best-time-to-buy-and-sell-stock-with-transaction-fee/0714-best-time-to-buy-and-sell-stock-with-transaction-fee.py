class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        memo = [[0] * 2 for _ in range(length + 1)]
        
        for index in range(length - 1, -1, -1):
            for j in range(2):
                if not j:
                    #selling
                    memo[index][j] = max(memo[index+1][j], memo[index+1][1] + prices[index] - fee)
                else:
                    #buying
                    memo[index][j] = max(memo[index+1][j], memo[index+1][0] - prices[index])
                    
        return memo[0][1]