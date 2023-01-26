class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        counter = 0
        
        for row in range(len(grid)-2):
            for col in range(len(grid)-2):
                temp_grid = [grid[row + element][col:col+3] for element in range(3)]
                print(temp_grid, row, col, len(grid))
                
                check_nums = [num for row in temp_grid for num in row]
                if sorted(check_nums) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    continue

                row_sums = [sum(row) for row in temp_grid]
                col_sums = [sum([row[i] for row in temp_grid]) for i in range(3)]
                diag_sums = [sum([temp_grid[i][i] for i in range(3)]), (temp_grid[0][2] + temp_grid[1][1] + temp_grid[2][0])]
                
                row_sums.extend(col_sums)
                row_sums.extend(diag_sums)
                
                
                if len(set(row_sums)) == 1:
                    counter += 1
        
        return counter
        
    

        