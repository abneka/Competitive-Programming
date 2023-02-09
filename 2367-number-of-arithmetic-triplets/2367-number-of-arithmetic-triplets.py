class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        ans = 0
        length = len(nums)
        for i in range(length):
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
                ans += 1
        
        return ans