class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0])
        bottom =  0
        res = float('inf')
        for top_g, bottom_g in zip(grid[0], grid[1]):
            top -= top_g
            res = min(res, max(top, bottom))
            bottom += bottom_g
        return res