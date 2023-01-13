class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        counter = collections.Counter()
        
        for row_index, row in enumerate(matrix):
            for col_index, col in enumerate(row):
                if counter[str(col_index - row_index)]:
                    if counter[str(col_index - row_index)] != col + 1:
                        return False
                counter[str(col_index - row_index)] = col + 1
            
        return True