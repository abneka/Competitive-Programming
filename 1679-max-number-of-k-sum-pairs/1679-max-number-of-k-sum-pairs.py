class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l, r = 0 , len(nums)-1
        result, total = 0, 0
        
        while l < r:
            total = nums[r] + nums[l]
            
            if total == k:
                result += 1
                l += 1
                r -= 1
            elif total < k:
                l += 1
            else:
                r -= 1
        
        return result
    
# 1 1 1 1 2 2 2 2