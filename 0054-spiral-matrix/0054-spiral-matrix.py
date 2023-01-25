class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_length = len(matrix)
        col_length = len(matrix[0])
        
        col_offset = 0
        row_offset = 0
        
        row = 0
        col = 0
        
        result = []
        
        while col != (col_length - col_offset) and row >= row_offset:
            for y in range(col, (col_length - col_offset)):
                result.append(matrix[row] [y])
                col = y
            
            row += 1
            # print('===>', str(row), str((row_length - row_offset)))
            if row >= (row_length - row_offset):
                break
            
            for x in range(row, ((row_length) - row_offset)):
                # print('==>', str(x))
                result.append(matrix[x] [col])
                row = x
            
            row_offset += 1
            
            col -= 1
            if col < 0:
                break
            
            for y in range(col, col_offset - 1, -1):
                # print(y)
                result.append(matrix[row][y])
                col = y
                
            row -= 1
            # print(row, row_offset)
            if row < row_offset or col < col_offset:
                break
                
            # print(str(row), '<==')
            # print(str(col), '<==')
            # print(col_offset, row_offset)
            # print(result)
            for x in range(row, row_offset-1, -1):
                # print(x)
                # print(result, col, row, row_offset)
                result.append(matrix[x][col])
                row = y
            
            
            col += 1
            row += 1
                
            
            
            col_offset += 1
            
        return result
            
            