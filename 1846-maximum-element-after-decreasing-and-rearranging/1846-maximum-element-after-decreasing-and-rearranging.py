class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        curr = 1
        
        for num in arr:
            if abs(curr - num) <= 1:
                curr = num
                continue
            
            curr += 1
        
        return curr