class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff = max(nums) - min(nums)
        return 0 if diff <= 2 * k else diff - (2 * k)