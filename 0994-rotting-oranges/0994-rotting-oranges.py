class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        max_row = len(grid)
        max_col = len(grid[0])
        remaining = 0
        
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if col == 1:
                    remaining += 1
                if col == 2:
                    queue.append((row_index, col_index))
                    
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        
        time = 0
        
        while queue:
            queue_size =  len(queue)
            total = 0
            length = 0
            while queue_size:
                row, col = queue.popleft()
                
                for move in moves:
                    next_row, next_col = move
                    if row +  next_row == max_row or col + next_col == max_col:
                        continue
                    if col + next_col < 0 or row +  next_row < 0:
                        continue
                    value = grid[row +  next_row] [col + next_col]
                    
                    if not value or value == 2:
                        continue
                        
                    queue.append((row +  next_row, col + next_col))
                    grid[row +  next_row] [col + next_col] = 2
                    remaining -= 1
                
                queue_size -= 1
            if not queue:
                break
            time += 1
            
        if remaining:
            return -1
        return time