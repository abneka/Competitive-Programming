class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even, odd = 0, 0
        
        for index in range(len(nums) - 1, -1, -1):
            max_even = max(even, odd + nums[index])
            max_odd = max(odd, even - nums[index])
            
            even, odd = max_even, max_odd
        
        return even