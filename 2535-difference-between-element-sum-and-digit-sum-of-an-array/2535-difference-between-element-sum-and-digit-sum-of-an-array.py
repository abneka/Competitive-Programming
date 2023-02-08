class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem = 0
        digit = 0
        
        for num in nums:
            elem += num
            string = str(num)
            string = [int(digit) for digit in string]
            digit += sum(string)
        
        return abs(elem - digit)