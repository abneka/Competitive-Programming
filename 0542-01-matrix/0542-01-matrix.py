class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        max_row = len(mat)
        max_col = len(mat[0])
        inbound = lambda row, col : 0 <= row < max_row and 0 <= col < max_col
        
        queue = deque()
        visited = set()
        
        for r, row in enumerate(mat):
            for c, col in enumerate(row):
                if not col:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        while queue:
            row, col, distance = queue.popleft()
            mat[row][col] = distance
            
            for r, c in moves:
                if (row + r, col + c) not in visited and inbound(row + r, col + c):
                    visited.add((row + r, col + c))
                    queue.append((row + r, col + c, distance + 1))
        
        return mat