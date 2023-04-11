class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        width = len(image[0])
        height = len(image)
        
        def dfs(curr, visited):
            row, col  = curr
            
            if col == width or row == height or col < 0 or row < 0:
                return
            
            if not image[row][col] == starting:
                return
                
            image[row][col] = color
            visited.add(curr)
            for next_row, next_col in direction:
                next_pos = (row + next_row, col + next_col)
                if next_pos in visited:
                    continue
                
                dfs(next_pos, visited)
        
        dfs((sr, sc), set())
        return image
        