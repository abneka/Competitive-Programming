class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.sum = [[0] * (col + 1)  for r in range(row+1)]
        
        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                
                self.sum[r+1][c+1] = prefix + self.sum[r][c+1]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        rightb = self.sum[row2][col2]
        above = self.sum[row1 - 1][col2]
        left = self.sum[row2][col1 - 1]
        add_on = self.sum[row1 - 1][col1 - 1]
        
        return rightb - above - left + add_on
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)