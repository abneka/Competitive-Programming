class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        edgeCount = [0]* n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            edgeCount[a] += 1
            edgeCount[b] += 1

        queue = deque()
        
        for node in range(n):
            if edgeCount[node] <= 1:
                queue.append(node)

        while n > 2:
            for _ in range(len(queue)):
                node = queue.popleft()
                edgeCount[node] -= 1
                n -= 1
                
                for neighbor in graph[node]:
                    if edgeCount[neighbor] - 1 == 1:
                        queue.append(neighbor)
                    edgeCount[neighbor] -= 1
        
        return queue