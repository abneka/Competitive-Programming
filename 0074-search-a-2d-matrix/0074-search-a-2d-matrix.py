class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        
        if rows == 1:
            if target in matrix[0]:
                return True
            else:
                return False
        
        for row in range(rows - 1):
            if target >= matrix[row][0] and target < matrix[row + 1][0]:
                if target in matrix[row]:
                    return True
        
        if target in matrix[rows - 1]:
            return True
                
        return False