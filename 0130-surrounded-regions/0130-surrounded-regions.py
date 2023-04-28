class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        
        max_row = len(board)
        max_col = len(board[0])
        start = []
        inbound = lambda row, col : 0 <= row < max_row and 0 <= col < max_col
        
        not_surrounded = set()
        def dfs(row, col):
            if board[row][col] == 'X' or (row, col) in not_surrounded:
                return
            
            not_surrounded.add((row, col))
            
            for next_row, next_col in moves:
                if inbound(next_row + row, next_col + col):
                    dfs(next_row + row, next_col + col)
        
        for row in range(max_row):
            dfs(row, 0)
            dfs(row, max_col - 1)
        
        for col in range(max_col):
            dfs(0, col)
            dfs(max_row - 1, col)
        
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if (row_index, col_index) not in not_surrounded:
                    board[row_index][col_index] = 'X'