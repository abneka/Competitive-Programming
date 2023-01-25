class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        one_dimensional = []
        result = []
        temp = []
        col_count = c
        
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        for row in mat:
            for num in row:
                one_dimensional.append(num)
        
        for row in mat:
            for col in row:
                
                if col_count:
                    temp.append(col)
                    col_count -= 1
                    continue
                col_count = c
                print(temp)
                result.append(temp)
                temp = []
                temp.append(col)
                col_count -= 1
        
        if temp:
            result.append(temp)
        
        return result