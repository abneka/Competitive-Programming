class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        result = 0
        
        while(r > l):
            result = max(result, (nums[l] + nums[r]))
            r -= 1
            l += 1
        
        return result
