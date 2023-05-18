class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
            
        queue = deque()
        visited = set()
        ans = []
        
        for key in indegree.keys():
            if indegree[key] == 1:
                queue.append(key)
                visited.add(key)
                break
        
        while queue:
            node = queue.popleft()
            
            ans.append(node)
            visited.add(node)
            
            for neigh in graph[node]:
                if neigh not in visited:
                    queue.append(neigh)
            
        return ans