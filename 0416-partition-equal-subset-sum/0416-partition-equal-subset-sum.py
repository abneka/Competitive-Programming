class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        total = sum(nums)
        half = total // 2
        if total % 2:
            return False
        
        memo = set()
        memo.add(0)
        for num in nums:
            new = set()
            for part in memo:
                if part + num == half:
                    return True
                new.add(part + num)
                new.add(part)
            memo = new
        
        return False