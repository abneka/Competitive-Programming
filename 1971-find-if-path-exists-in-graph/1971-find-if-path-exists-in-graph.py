class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
        stack = [source]
        visited = set()
        
        while stack:
            if stack[-1] in visited:
                stack.pop()
                continue
                
            if stack[-1] == destination:
                return True
            visited.add(stack[-1])
            stack.extend(graph[stack.pop()])
        
        return False
                
            
#         def dfs(visited, vertex):
#             if vertex == destination:
#                 return True
#             visited.add(vertex)
#             flag = False
            
#             for negi in graph[vertex]:
#                 if negi not in visited:
#                     flag = flag or dfs(visited, negi)
                    
#             return flag
        
#         return dfs(set(), source)