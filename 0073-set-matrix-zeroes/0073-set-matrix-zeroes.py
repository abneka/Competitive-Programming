class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row_length = len(matrix)
        col_length = len(matrix[0])
        
        def default():
            return 1
        
        rows = defaultdict(default)
        cols = defaultdict(default)

        for i in range(row_length):
            for j in range(col_length):
                if matrix[i][j] == 0:
                    rows[str(i)] = 0
                    cols[str(j)] = 0

        for i in range(row_length):
            for j in range(col_length):
                if not rows[str(i)] or not cols[str(j)]:
                    matrix[i][j] = 0