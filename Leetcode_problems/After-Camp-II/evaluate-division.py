class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (var1, var2), val in zip(equations, values):
            graph[var1].append((var2, val))
            graph[var2].append((var1, 1/val))
        
        def dfs(start, end, value):
            if start == end:
                return value
            
            visited.add(start)
            ans = -1
            for next_vertex, val in graph[start]:
                if not next_vertex in visited:
                    ans = max(dfs(next_vertex, end, value * val), ans)
            
            return ans
        
        answer = []
        for start, end in queries:
            visited = set()
            if not start in graph:
                answer.append(-1)
                continue
            answer.append(dfs(start, end, 1))
            
        return answer