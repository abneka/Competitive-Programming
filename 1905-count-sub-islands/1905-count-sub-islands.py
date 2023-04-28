class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        
        max_row = len(grid1)
        max_col = len(grid1[0])
        inbound = lambda row, col : 0 <= row < max_row and 0 <= col < max_col
        start = []
        
        for row_index, row in enumerate(grid1):
            for col_index, col in enumerate(row):
                if col == 1 and grid2[row_index][col_index] == 1:
                    start.append((row_index, col_index))
                    continue
                
        visited = set()
        def dfs(row, col):
            if not grid1[row][col] and grid2[row][col] or (row, col) in visited:
                return 0
            
            if not grid2[row][col]:
                return 1
            visited.add((row, col))
            result = 1
            for next_row, next_col in moves:
                if (next_row + row, next_col + col) in visited:
                    continue
                    
                if inbound(next_row + row, next_col + col):
                    result *= dfs(next_row + row, next_col + col)
                
            return result
        
        result = 0
        for row, col in start:
            result += dfs(row, col)
        return result