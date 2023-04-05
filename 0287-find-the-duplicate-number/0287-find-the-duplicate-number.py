class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sort = [0] * len(nums)
        
        for num in nums:
            if sort[num - 1]:
                return num
            sort[num - 1] = num