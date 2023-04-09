class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        a/b = 2
        a = 2b
        b/c = 3
        3 X 2
        = > a/c = 6
        c/d = 4
        3 X 2 X 4
        a/d = 24
        b/a = 0.5
        a -> b = 2 -> b => c = 3 -> b => a = 1/2
        graph = {a:[(2, b)], b:[(3,c)]}
        dfs(a, c)
        1/dfs(c, a)
        a => e = 4 -> b => e = 3
        '''
        graph = defaultdict(list)
        for index, (start, end) in enumerate(equations):
            graph[start].append((values[index], end))
            graph[end].append((1/values[index], start))
            
        def dfs(start, end, value, visited):
            if start == end:
                return (True, value)
            
            visited.add(start)
            
            for val, next_vertex in graph[start]:
                if next_vertex in visited:
                    continue
                found, answer = dfs(next_vertex, end, value * val, visited)
                if found:
                    return (found, answer)
            
            return (False, value)
        
        answer = []
        for start, end in queries:
            found, ans = dfs(start, end, 1, set())
            if found and start in graph:
                answer.append(ans)
                continue
            
            answer.append(-1)
            
        return answer
                    