class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sub = sum(nums[:k])
        length = len(nums)
        
        left = 0
        right = k
        
        maxi = sub
        new = sub
        
        while right < length:
            new = new - nums[left] + nums[right]
            maxi = max(maxi, (new))
            left += 1
            right += 1
        
        
        return maxi/k