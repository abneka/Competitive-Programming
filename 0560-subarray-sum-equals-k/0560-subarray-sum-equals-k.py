class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pSum = {0: 1}
        total= res = 0
        
        for i in nums:
            total += i
            if total - k in pSum:
                res += pSum[total-k]
            
            if total in pSum:
                pSum[total] += 1   
                continue
            
            pSum[total] = 1
        
        return res