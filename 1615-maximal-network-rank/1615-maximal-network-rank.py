class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for start, end in roads:
            graph[start].add(end)
            graph[end].add(start)
            
        maxi = 0
        
        for start in range(n):
            for end in range(start + 1, n):
                maxi = max(maxi, len(graph[start]) + len(graph[end]) - (start in graph[end]))
        return maxi