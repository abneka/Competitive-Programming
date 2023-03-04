class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        root = 0

        while left <= right:
            mid = (left + right) // 2
            if (mid * mid) == x:
                root = mid
                break
                
            if (mid * mid) > x:
                right = mid - 1
                
            else:
                left = mid + 1
                root = mid
        return root