class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        memo = [[-1] * 2 for _ in range(length)]
        if length == 1:
            return nums[0]
        def rob (n, flag):
            if n < 0:
                return 0
            if n <= 1:
                if not n and flag:
                    if nums[0] > nums[length - 1]:
                        return nums[0] - nums[length -1]
                    return 0
                return nums[n]
            
            if memo[n][flag] == -1:
                memo[n][flag] = max(rob(n-2, flag) + nums[n], rob(n-3, flag) + nums[n])
            
            return memo[n][flag]
        return max(rob(length - 1, 1), rob(length - 2, 0))