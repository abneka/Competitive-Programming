class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        visited = set()
        
        def dfs(row, col, depth):
            if (row, col) in visited:
                return 0
            
            if row == max_row or col == max_col or row < 0 or col < 0 or not grid[row][col]:
                return 0
            
            visited.add((row, col))
            total = 1
            for move in moves:
                move_r, move_c = move
                total += dfs(row + move_r, col + move_c, depth + 1)
            
            return total
        
        
        maxi = 0
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if not col or (r,c) in visited:
                    continue
                maxi = max(dfs(r, c, 1), maxi)
        
        return maxi