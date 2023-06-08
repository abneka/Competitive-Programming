class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        left = 0
        col = len(grid[0])
        right = col - 1
        ans = 0
        for row in range(len(grid)):
            while left <= right:
                mid = (left + right) // 2
                
                if grid[row][mid] >= 0:
                    left = mid + 1

                else:
                    right = mid - 1

            if grid[row][mid] >= 0:
                mid += 1
            
            left = 0
            right = mid -1
            ans += (col - mid)
        return ans