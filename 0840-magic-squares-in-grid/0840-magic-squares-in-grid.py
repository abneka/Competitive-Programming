class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        # Construct the 3x3 square
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                temp_grid = [grid[i+k][j:j+3] for k in range(3)]
                print(temp_grid, i, j, len(grid))
                if self.isMagicSquare(temp_grid):
                    cnt += 1
        
        return cnt
        
    
    def isMagicSquare(self, grid):
        '''
        Check whether the given grid is a magic square
        '''
        # Check the elements
        flat = [num for row in grid for num in row]
        if sorted(flat) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        
        # Check the row, column and diagnal sums
        row_sums = [sum(row) for row in grid]
        col_sums = [sum([row[i] for row in grid]) for i in range(3)]
        diag_sums = [sum([grid[i][i] for i in range(3)]), (grid[0][2] + grid[1][1] + grid[2][0])]
        row_sums.extend(col_sums)
        row_sums.extend(diag_sums)
        return len(set(row_sums)) == 1