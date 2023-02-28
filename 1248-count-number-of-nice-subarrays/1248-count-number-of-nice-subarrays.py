class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = Counter()
        prefix_sum[0] = 1
        
        total = 0
        count = 0
        
        for num in nums:
            if not num % 2:
                num = 0
            else:
                num = 1
            total += num
            
            if prefix_sum[total - k]:
                count += prefix_sum[total-k]
            
            prefix_sum[total] += 1
        
        
        return count
