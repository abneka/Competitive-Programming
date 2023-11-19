# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        
        l, r = 1, length - 2
        # find the index of peak
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountain_arr.get(m - 1), mountain_arr.get(m), mountain_arr.get(m + 1)
            
            if left < mid < right:
                l = m + 1
            
            elif left > mid > right:
                r = m - 1
            
            else:
                break
        peak = m
        #search the strictly increasing part
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            mid = mountain_arr.get(m)
            
            if mid < target:
                l = m + 1
            
            elif mid > target:
                r = m - 1
            
            else:
                return m
        #search the strictly decreasing part
        l, r = peak, length - 1
        while l <= r:
            m = (l + r) // 2
            mid = mountain_arr.get(m)
            
            if mid > target:
                l = m + 1
            
            elif mid < target:
                r = m - 1
            
            else:
                return m
        #not found on the whole array
        return -1
        