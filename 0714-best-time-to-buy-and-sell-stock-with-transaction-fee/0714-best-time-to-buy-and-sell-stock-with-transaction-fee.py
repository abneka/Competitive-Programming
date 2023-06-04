class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        memo = [0, 0]
        
        for index in range(length - 1, -1, -1):
            for j in range(2):
                if not j:
                    #selling
                    memo[j] = max(memo[j], memo[1] + prices[index] - fee)
                else:
                    #buying
                    memo[j] = max(memo[j], memo[0] - prices[index])
                    
        return memo[1]