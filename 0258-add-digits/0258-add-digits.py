class Solution:
    def addDigits(self, num: int) -> int:
        digits = str(num)
        
        while len(digits) - 1:
            total = 0
            
            for digit in digits:
                total += int(digit)
                
            digits = str(total)
        
        return int(digits)