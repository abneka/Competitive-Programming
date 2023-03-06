class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        
        res = right
        
        while left <= right:
            divisor = (left + right) // 2
            
            total = 0
            
            for num in nums:
                total += math.ceil(num / divisor)
            
            if total <= threshold:
                res = divisor
                right = divisor - 1
            
            else:
                left = divisor + 1
        
        return res