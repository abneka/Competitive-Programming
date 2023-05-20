class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(int)
        rank = defaultdict(int)
        
        for node in range(len(edges)):
            graph[node] = node
            rank[node] += 1
        
        def find(node):
            if graph[node] != node:
                graph[node] = find(graph[node])
            return graph[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if parent1 == parent2:
                return False
            
            if rank[parent1] > rank[parent2]:
                graph[parent2] = parent1
                rank[parent1] += rank[parent2]
            
            else:
                graph[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]