class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        inbound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        nextgrid = lambda row, col, move: (moves[move][0] + row , moves[move][1] + col)
        parent = [node for node in range(rows*cols)]
        rank = [1 for _ in range(rows*cols)]
        moves = [(0,-1),(0,1),(-1,0),(1,0)]
#                left-0  right-1 up-2   down-3
        street = {1:[0,1],2:[2,3],3:[0,3],4:[1,3],5:[0,2],6:[1,2]}
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            if rank[parent1] < rank[parent2]: 
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
        test = []
        for row in range(rows):
            for col in range(cols):
                for move in street[grid[row][col]]:
                    x, y = nextgrid(row, col, move)
                    if move % 2:
                        move -= 2
                    move += 1
                    if inbound(x, y) and move in street[grid[x][y]]:
                        union(row*cols+col,x*cols+y)
        return find(0) == find(rows * cols - 1)
    
