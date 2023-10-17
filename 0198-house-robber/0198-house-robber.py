class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * 2
        memo.extend([num for num in nums])
        
        for index in range(3, len(nums) + 2):
            memo[index] = max(memo[index - 2] + memo[index], memo[index - 3] + memo[index])
        
        return max(memo[-1], memo[-2])
        
#         @cache
#         def climb (n):
            
#             if n < 0:
#                 return 0
#             if n <= 1:
#                 return nums[n]
            
#             return max(climb(n-2) + nums[n], climb(n-3) + nums[n])
            
        
        return max(climb(len(nums) - 1), climb(len(nums) - 2))