class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        square = [[set() for i in range(3)] for _ in range(3)]
        
        for r in range(9):
            row = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in row or 
                    board[r][c] in cols[c] or 
                    board[r][c] in square[r //3][c // 3]):
                    return False
                
                row.add(board[r][c])
                cols[c].add(board[r][c])
                square[r // 3][c // 3].add(board[r][c])
        return True