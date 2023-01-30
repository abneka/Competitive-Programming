class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        length = int(math.sqrt(c))
        # print(length)
        left = 0
        right = length
        # print(left, right)
        
        while left <= right:
            
            left_sqr = left ** 2
            right_sqr = right ** 2
            total = left_sqr + right_sqr
            
            # print(total, left, right)
            
            if total > c:
                right -= 1
            
            elif total < c:
                left += 1
                
            else:
                return True
        
        return False