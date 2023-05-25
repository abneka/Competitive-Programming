class Solution:
    def minDifference(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 4:
            return 0
        nums.sort()
        mini = float('inf')
        for index in range(4):
            mini = min(nums[index + length - 4] - nums[index], mini)
            
        return mini