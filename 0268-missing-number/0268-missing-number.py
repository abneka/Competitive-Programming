class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)+1 #length of number including the missing number
        
        for num in range(length):
            if num not in nums:
                return num #return the number if it is not in the list