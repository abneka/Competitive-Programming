class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        
        if n < 3:
            return arr[n]
        
        for num in range(3, n + 1):
            temp = sum(arr)
            arr[0] = arr[1]
            arr[1] = arr[2]
            arr[2] = temp
        
        return arr[-1]
