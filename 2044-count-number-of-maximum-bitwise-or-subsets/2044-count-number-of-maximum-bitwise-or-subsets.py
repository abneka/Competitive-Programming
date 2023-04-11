class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = defaultdict(int)
        n = 2**len(nums)
        for i in range(n):
            check = 0
            for j in range(len(nums)):
                if i >> j & 1:
                    check |= nums[j]
            count[check] += 1
            
        return count[max(count)]