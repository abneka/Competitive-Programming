class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        memo = [1] * length
        ans = 1

        for index in range(length, -1, -1):
            for ind in range(index + 1, length):
                if nums[index] < nums[ind]:
                    memo[index] = max(memo[index], memo[ind] + 1)
                    ans = max(ans, memo[index])
        
        return ans