class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(row, col, visited):
            if (row, col) in visited:
                return visited
            if row == max_row or col == max_col or row < 0 or col < 0 or not grid[row][col]:
                return visited
            
            visited.add((row, col))
            
            for move in moves:
                move_r, move_c = move
                visited.update(dfs(row + move_r, col + move_c, visited))
            
            return visited
        
        
        visited = set()
        maxi = 0
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if not col or (r,c) in visited:
                    continue
                
                new = dfs(r,c,set())
                maxi = max(maxi, len(new))
                visited.update(new)
        
        return maxi