class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        memo = [0, 0]
        
        for index in range(length - 1, -1, -1):
            #selling
            memo[0] = max(memo[0], memo[1] + prices[index] - fee)
            #buying
            memo[1] = max(memo[1], memo[0] - prices[index])
                    
        return memo[1]