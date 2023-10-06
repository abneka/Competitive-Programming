class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for v, u, w in times:
            graph[v].append((w, u))
        
        queue = [(0, k)]
        distance = [float('inf')] * (n + 1)
        distance[k] = 0
        distance[0] = 0
        visited = set()
        
        while queue:
            currW, node = heappop(queue)
            if node in visited:
                continue
            
            visited.add(node)
            
            for weight, neigh in graph[node]:
                dist = currW + weight
                
                if distance[neigh] > dist:
                    distance[neigh] = dist
                    heappush(queue, (dist, neigh))
        
        return -1 if any(d == float('inf') for d in distance) else max(distance)