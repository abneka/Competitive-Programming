class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = {}
        
        for char in range(ord('a'), ord('z') + 1):
            graph[chr(char)] = chr(char)
        
        def find(node):
            if graph[node] != node:
                graph[node] = find(graph[node])
            return graph[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            mini = min(parent2, parent1)
            
            graph[parent1] = mini
            graph[parent2] = mini
        
        for char1, char2 in zip(s1, s2):
            union(char1, char2)
        
        ans = ''
        for char in baseStr:
            ans += find(char)
            
        return ans