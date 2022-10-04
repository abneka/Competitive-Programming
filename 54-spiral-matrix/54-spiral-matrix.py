class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result.extend(matrix[0])
            matrix.pop(0)
            
            if not matrix:
                break
                
            for i in range(len(matrix)-1):
                if matrix[i]:
                    result.append(matrix[i].pop())
                    
            result.extend(matrix[-1][::-1])
            matrix.pop()
            
            for i in range(len(matrix)-1, 0, -1):
                if matrix[i]:
                    result.append(matrix[i][0])
                    matrix[i].pop(0)
            
        return result