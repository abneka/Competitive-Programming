class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [1] * n
        checkCol = lambda col: 0 <= col < n
        
        for row in range(1, m):
            for col in range(n):
                if checkCol(col - 1):
                    arr[col] += arr[col - 1]
        
        return arr[-1]