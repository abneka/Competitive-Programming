class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        destination = length * length
        right = length % 2
        
        def convert(square):
            row = length - ((square - 1) // length) - 1
            
            if (row + right) % 2:
                return (row, ((square - 1) % length))
            
            else:
                return (row, (length -1) - ((square - 1) % length))
        
        queue = deque()
        queue.append((1, 0))
        visited = set()
        
        while queue:
            square, moves = queue.popleft()
            
            for die in range(1, 7):
                next_square = square + die
                row, col = convert(next_square)
                
                if board[row][col] != -1:
                    next_square = board[row][col]
                
                if next_square == destination:
                    return moves + 1
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1