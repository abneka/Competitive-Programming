class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        moves = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        max_row = len(board)
        max_col = len(board[0])
        inbound = lambda row, col: 0 <= row < max_row and 0 <= col < max_col
        
        queue = deque([(click[0], click[1])])
        visited = set()
        
        while queue:
            row, col = queue.popleft()
            
            val = 0
            
            new = []
            new_set = set()
            for r, c in moves:
                if (row + r, col + c) not in visited and inbound(row + r, col + c):
                    if board[row + r][col + c] == 'M':
                        val += 1
                        continue
                    new_set.add((row + r, col + c))
                    new.append((row + r, col + c))
            
            if board[row][col] == 'M':
                board[row][col] = 'X'
                break
            
            elif val:
                board[row][col] = str(val)
            
            else:
                queue.extend(new)
                visited.update(new_set)
                board[row][col] = 'B'
            
        return board
                    