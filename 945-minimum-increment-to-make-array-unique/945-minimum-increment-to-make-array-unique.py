class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i+1] += 1
                res += 1
                
            elif nums[i] > nums[i+1]:
                diff = nums[i]-nums[i+1]+1
                nums[i+1] += diff
                res += diff
                
        return res