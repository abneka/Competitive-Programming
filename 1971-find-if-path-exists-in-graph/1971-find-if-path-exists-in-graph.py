class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(int)
        
        for node in range(n):
            graph[node] = node
            
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if parent1 != parent2:
                graph[parent1] = parent2
            
        def find(node):
            while graph[node] != node:
                node = graph[node]
            
            return node
        
        for u, v in edges:
            union(u, v)
        
        return find(source) == find(destination)