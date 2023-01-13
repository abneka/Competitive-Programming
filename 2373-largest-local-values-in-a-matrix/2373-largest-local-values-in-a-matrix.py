class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        result = [[0] * (length -2) for i in range(length - 2)]
        
        for row in range(length - 2):
            for col in range(length - 2):
                
                bottom_up = max(grid[row][col + 1], grid[row + 2][col + 1])
                
                right_left = max(grid[row + 1][col], grid[row + 1][col + 2])
                
                diagonal_1 = max(grid[row][col], grid[row + 2][col + 2])
                
                diagonal_2 = max(grid[row][col + 2], grid[row + 2][col])
                
                maximum = max(bottom_up, right_left, diagonal_1, diagonal_2, grid[row + 1] [col + 1])
                
                result[row][col] = maximum
            
        return result