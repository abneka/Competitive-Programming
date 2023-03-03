# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        mid = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if isBadVersion(mid):
                high = mid - 1
                if mid and not isBadVersion(high):
                    return mid
            
            else:
                low = mid + 1
                if low <= high and isBadVersion(low):
                    return mid + 1
