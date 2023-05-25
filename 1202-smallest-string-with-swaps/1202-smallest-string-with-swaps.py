class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        length = len(s)
        parent = [i for i in range(length)]
        size = [0] * length
        ans = list(s)
        graph = defaultdict(list)
        ans = ''

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if size[parent1] > size[parent2]:
                parent[parent2] = parent1
                size[parent1] += size[parent2]
            else:
                parent[parent1] = parent2
                size[parent2] += size[parent1]
        
        for x,y in pairs:
            union(x,y)

        for i in range(length):
            graph[find(i)].append(s[i])
            
        for key in graph.keys():
            graph[key].sort(reverse = True)
            
        for index in range(length):
            ans += graph[find(index)].pop()
     
        return ans