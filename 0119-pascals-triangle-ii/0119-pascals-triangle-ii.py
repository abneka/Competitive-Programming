class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        memo = {}
        def findArray(row, col):
            if not row or not col or row == 1 or row == col:
                return 1
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            memo[(row, col)] = (findArray(row - 1, col - 1) + findArray(row - 1, col))
            
            return memo[(row, col)]
            
            # return (findArray(row - 1, col - 1) + findArray(row - 1, col))
        
        array = []
        for col in range(rowIndex +1):
            array.append(findArray(rowIndex, col))
        
        return array