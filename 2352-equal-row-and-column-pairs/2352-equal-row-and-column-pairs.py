class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = collections.Counter()
        
        total = 0
        row_size = len(grid)
        
        for row in grid:
            counter[tuple(row)] += 1
            
        for index in range(row_size):
            
            col = []
            
            for row in grid:
                col.append(row[index])
            
            total += counter[tuple(col)]
        
        return total