class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = []
        total = 1
        
        for i in nums:
            res.append(total)
            total *= i 
        total = 1
        
        for i in range(length-1, -1, -1):
                res[i] *= total
                total *= nums[i]
            
        return res