class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        graph_row = defaultdict(list)
        graph_col = defaultdict(list)
        
        row_indeg = [0] * (k + 1)
        col_indeg = [0] * (k + 1)
        

        matrix = [[0]*k for i in range(k)]
        
        for indep, dep in rowConditions:
            graph_row[indep].append(dep)
            row_indeg[dep] += 1
        
        for indep, dep in colConditions:
            graph_col[indep].append(dep)
            col_indeg[dep] += 1
        
        def reorder(graph, indeg):
            ans = {}
            queue = deque()
            index = 0
            
            for node in range(1, k + 1):
                if not indeg[node]:
                    queue.append(node)
                    
            while queue:
                node = queue.popleft()
                ans[node] = index
                index += 1
                for child in graph[node]:
                    indeg[child] -= 1
                    if not indeg[child]:
                        queue.append(child)
            return ans

        rows = reorder(graph_row,row_indeg)
        cols  = reorder(graph_col,col_indeg)
        
        for index in range(1, k + 1):
            if index in rows and index in cols:
                matrix[rows[index]][cols[index]] = index
                continue
            return []

        return matrix