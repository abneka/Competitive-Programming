class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        memo = {}
        def dp(index, val):
            if index == length:
                if val == target:
                    return 1
                return 0
            
            state = (index, val)
            
            if state not in memo:
                positive = dp(index + 1, val + nums[index])
                negative = dp(index + 1, val - nums[index])

                memo[state] = positive + negative
                
            return memo[state]
            
            
        return dp(0, 0)
