class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        inbound = lambda row, col: row <= m and col <= n
        def path(row, col):
            if not inbound(row, col):
                return 0
            
            if row == m and col == n:
                return 1
            
            if memo[row - 1][col - 1] == -1:
                memo[row - 1][col - 1] = path(row + 1, col) + path(row, col + 1)
            
            return memo[row - 1][col - 1]
        
        return path(1, 1)