class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        max_row = len(maze)
        max_col = len(maze[0])
        inbound = lambda row, col : 0 <= row < max_row and 0 <= col < max_col and maze[row][col] == '.'
        is_exit = lambda row, col : not col or not row or col == max_col - 1 or row == max_row - 1
        
        queue = deque([(entrance[0], entrance[1])])
        visited = set()
        count = 0
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if is_exit(row, col) and [row, col] != entrance:
                    return count

                for r, c in moves:
                    if (row + r, col + c) not in visited and inbound(row + r, col + c):
                        visited.add((row + r, col + c))
                        queue.append((row + r, col + c))
            count += 1
        
        return -1
                    