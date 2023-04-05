class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pos = 0
        
        for num in nums:
            index = num - 1
            
            if pos & (1<<index):
                return num
            
            pos = pos | (1<<index)