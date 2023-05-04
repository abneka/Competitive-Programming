class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        moves = [(1,1), (1,0), (-1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,-1)]
        length = len(grid)
        inbound = lambda row, col : 0 <= row < length and 0 <= col < length and grid[row][col] == 0
        
        if grid[0][0] == 1:
            return -1
        
        queue = deque([(0,0)])
        count = 1
        visited = set()
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                row, col = queue.popleft()
                print(row, col)
                if row == length - 1 and col == length - 1:
                    return count
                
                for r, c in moves:
                    if (row + r, col + c) not in visited and inbound(row + r, col + c):
                        visited.add((row + r, col + c))
                        queue.append((row + r, col + c))
            
            count += 1
        
        return -1