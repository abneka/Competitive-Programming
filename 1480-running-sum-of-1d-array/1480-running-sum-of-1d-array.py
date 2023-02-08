class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        
        for index, num in enumerate(nums):
            total += num
            nums[index] = total
        
        return nums