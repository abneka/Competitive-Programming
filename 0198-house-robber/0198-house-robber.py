class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1 for _ in range(len(nums))]
        
        def climb (n):
            
            if n < 0:
                return 0
            if n <= 1:
                return nums[n]
            
            if memo[n] == -1:
                memo[n] = max(climb(n-2) + nums[n], climb(n-3) + nums[n])
            
            return memo[n]
        
        return max(climb(len(nums) - 1), climb(len(nums) - 2))