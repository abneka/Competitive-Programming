class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        memo = [[-1] * 1001 for _ in range(length)]
        def dp(index, val):
            if index == length:
                if val == target:
                    return 1
                return 0
            
            if memo[index][val] == -1:
                positive = dp(index + 1, val + nums[index])
                negative = dp(index + 1, val - nums[index])

                memo[index][val] = positive + negative
                
            return memo[index][val]
            
            
        return dp(0, 0)
