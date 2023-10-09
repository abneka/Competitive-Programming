class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        
        for edge, prob in zip(edges, succProb):
            u, v = edge
            graph[u].append((v, prob))
            graph[v].append((u, prob))
            
        heap = [(-1, start_node)]
        max_prob = [0] * n
        visited = set()
        
        while heap:
            curr_prob, curr_node = heappop(heap)
            
            if curr_node == end_node: return -curr_prob
            
            if curr_node in visited: continue
            visited.add(curr_node)
            
            for neigh, prob in graph[curr_node]:
                new_prob = curr_prob * prob
                
                if new_prob < max_prob[neigh]:
                    max_prob[neigh] = new_prob
                    heappush(heap, (new_prob, neigh))
        return 0 