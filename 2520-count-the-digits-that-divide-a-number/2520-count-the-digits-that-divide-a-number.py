class Solution:
    def countDigits(self, num: int) -> int:
        string = str(num)
        count = 0
        
        for digit in string:
            if not num % int(digit):
                count += 1
        
        return count