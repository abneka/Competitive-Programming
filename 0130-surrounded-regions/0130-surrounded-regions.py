class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        
        max_row = len(board)
        max_col = len(board[0])
        start = []
        
        for row_index, row in enumerate(board):
            if row[0] == 'O':
                start.append((row_index, 0))
                
            if max_col > 1:
                if row[max_col - 1] == 'O':
                    start.append((row_index, max_col - 1))
                    
            if row_index == 0 or row_index == max_row - 1:
                for col in range(1, max_col - 1):
                    if row[col] == 'O':
                        start.append((row_index, col))
                    
        not_surrounded = set()
        def dfs(row, col):
            if row == max_row or col == max_col or col < 0 or row < 0:
                return
            
            if board[row][col] == 'X' or (row, col) in not_surrounded:
                return
            
            not_surrounded.add((row, col))
            for move in moves:
                next_row, next_col = move
                next_row += row
                next_col += col
                dfs(next_row, next_col)
        
        for row, col in start:
            dfs(row, col)
        
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if col == 'O' and (row_index, col_index) not in not_surrounded:
                    board[row_index][col_index] = 'X'