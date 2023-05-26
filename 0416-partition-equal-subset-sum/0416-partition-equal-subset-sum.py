class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        total = sum(nums)
        memo = {}
        
        def dp(index, curr):
            if not curr:
                return True
            
            if index == length or curr < 0:
                return False
            
            elif (index, curr) in memo:
                return memo[(index, curr)]
            
            memo[(index, curr)] = dp(index + 1, curr - nums[index]) or dp(index + 1, curr)
            return memo[(index, curr)]
        
        
        if total % 2: 
            return False 
        else: 
            return dp(0,total//2)
            