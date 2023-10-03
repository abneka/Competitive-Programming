class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((w, v))
        
        queue = [(0, k)]
        distance = [float('inf')] * n
        distance[k - 1] = 0
        visited = set()
        
        while queue:
            curr, node = heappop(queue)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for weight, neigh in graph[node]:
                dist = curr + weight
                
                if dist < distance[neigh - 1]:
                    distance[neigh - 1] = dist
                    heappush(queue, (dist, neigh))
                    
        return -1 if any(d == float('inf') for d in distance) else max(distance)