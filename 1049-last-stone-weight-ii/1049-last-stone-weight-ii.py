class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        biggest = stoneSum // 2
        length = len(stones)
        memo = {}

        def dp(index, total):
            if total >= biggest or index == length:
                return abs(total - (stoneSum - total))

            state = (index, total)

            if state not in memo:
                memo[state] = min(dp(index + 1, total), dp(index + 1, total + stones[index]))
            
            return memo[state]
        
        return dp(0,0)