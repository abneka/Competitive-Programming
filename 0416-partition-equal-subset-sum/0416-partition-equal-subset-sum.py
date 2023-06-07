class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        total = sum(nums)
        half = total // 2
        if total % 2:
            return False
        
        memo = set()
        
        for num in nums:
            temp = list(memo)
            for val in temp:
                memo.add(val + num)
            memo.add(num)
        
        return half in memo