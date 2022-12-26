class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) +1 #length of number with the missing number
        total = sum(num for num in range(length)) #sum of numbers with missing number
        return total - sum(nums) #difference between sum of expected and original value