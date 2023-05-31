class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[-1] * n for _ in range(m)]
        inbound = lambda row, col: 0<= row < m and 0<=col < n and not obstacleGrid[row][col]
        def path(row, col):
            if not inbound(row, col):
                return 0
            
            if row == m - 1  and col == n - 1:
                return 1
            
            if memo[row - 1][col - 1] == -1:
                memo[row - 1][col - 1] = path(row + 1, col) + path(row, col + 1)
            
            return memo[row - 1][col - 1]
        
        return path(0, 0)