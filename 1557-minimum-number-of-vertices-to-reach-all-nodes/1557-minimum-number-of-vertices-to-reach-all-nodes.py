class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = Counter()
        ans = []
        
        for start, end in edges:
            graph[end] += 1
        
        for start, end in edges:
            if not graph[start]:
                graph[start] += 1
                ans.append(start)
        
        return ans