class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [1] * m
        checkRow = lambda row: 0 <= row < m
        
        for col in range(1, n):
            for row in range(m):
                if checkRow(row - 1):
                    arr[row] += arr[row - 1]
        
        return arr[-1]