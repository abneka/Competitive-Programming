class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        width = len(image[0])
        height = len(image)
        
        def dfs(curr):
            row, col  = curr
            
            image[row][col] = color
            for next_row, next_col in direction:
                new_row = row + next_row
                new_col = col + next_col
                if new_col == width or new_row == height or new_col < 0 or new_row < 0:
                    continue
                if image[new_row][new_col] == color or not image[new_row][new_col] == starting:
                    continue
                
                dfs((new_row, new_col))
        
        dfs((sr, sc))
        return image
        