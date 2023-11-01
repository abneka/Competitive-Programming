class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [ [[-1] * 3 for opt in range(2)] for _ in range(len(prices))]
        def dp(index, opt, prices, limit, memo):
            if index == len(prices) or not limit:
                return 0
            if memo[index][opt][limit] == -1:
                profit = 0
                if not opt:
                    profit = max(dp(index + 1, 1, prices, limit, memo)
                                 -prices[index],
                                 dp(index + 1, 0, prices, limit, memo))
                else:
                    profit = max(dp(index + 1, 0, prices, limit - 1, memo)
                                 +prices[index],
                                 dp(index + 1, 1, prices, limit, memo))
                memo[index][opt][limit] = profit
            return memo[index][opt][limit]
        return dp(0,0,prices,2,memo)