class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        noDuplicate = list(dict.fromkeys(nums))
        result = 0
        for num in noDuplicate:
            for i in range(1, nums.count(num)):
                result += i
        return result