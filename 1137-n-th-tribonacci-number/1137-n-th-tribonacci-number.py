class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        
        if n < 3:
            return arr[n]
        
        for _ in range(3, n + 1):
            new = sum(arr)
            arr[0] = arr[1]
            arr[1] = arr[2]
            arr[2] = new
        
        return arr[-1]