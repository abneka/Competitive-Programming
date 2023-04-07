class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
        def dfs(visited, vertex):
            if vertex == destination:
                return True
            visited.add(vertex)
            flag = False
            
            for negi in graph[vertex]:
                if negi not in visited:
                    flag = flag or dfs(visited, negi)
                    
            return flag
        
        return dfs(set(), source)