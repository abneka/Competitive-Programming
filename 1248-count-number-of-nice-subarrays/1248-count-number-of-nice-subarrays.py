class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num%2 for num in nums]
        prefix = {0:1}
        total = 0
        res = 0
        for i in nums:
            total += i
            if total-k in prefix:
               res += prefix[total-k]
            
            if total in prefix:
                prefix[total] += 1
                continue
            
            prefix[total] = 1
            
        return res