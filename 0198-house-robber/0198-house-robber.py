class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def climb (n):
            
            if n < 0:
                return 0
            if n <= 1:
                return nums[n]
            
            return max(climb(n-2) + nums[n], climb(n-3) + nums[n])
            
        
        return max(climb(len(nums) - 1), climb(len(nums) - 2))