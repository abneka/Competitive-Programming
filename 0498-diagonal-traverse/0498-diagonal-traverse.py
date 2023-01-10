class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 0-0 0-1 1-0 
        
        res = []
        col = row = 0
        col_size = len(mat[0])
        row_size = len(mat)
        
        while col < col_size and row < row_size:
        
            while row > -1 and col < col_size:
                
                res.append(mat[row][col])
                row -= 1
                col +=1
            
            if col == col_size:
                col -= 1
                row += 1
            
            row += 1
            
            while row < row_size and col > -1:
                
                res.append(mat[row][col])
                row += 1
                col -= 1
            
            if row == row_size:
                col += 1
                row -= 1
                
            col += 1
        
        return res
            