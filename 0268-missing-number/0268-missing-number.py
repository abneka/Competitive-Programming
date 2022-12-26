class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) +1
        total = sum(num for num in range(length))
        return total - sum(nums)