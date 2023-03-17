class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        p_sum = Counter()
        
        p_sum[0] = 1
        total = 0
        ans = 0
        
        for num in nums:
            total += num
            
            if p_sum[total - goal]:
                ans += p_sum[total - goal]
            
            p_sum[total] += 1
        
        return ans