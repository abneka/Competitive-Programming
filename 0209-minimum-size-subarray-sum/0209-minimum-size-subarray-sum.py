class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l, r = 0, 0
        k = target
        ans = float('inf')
        while r < len(nums):
            
            while total < k and r < len(nums):
                total += nums[r]
                r += 1
            
            while total >= k:
                if r-1 == l:
                    return 1
                
                ans = min(ans, (r-l))
                total -= nums[l]
                l += 1
                
        if ans == float('inf'):
            return 0
        return ans