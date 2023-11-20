class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {src: [] for src, dest in tickets}
        tickets.sort(reverse=True)
        for src, dest in tickets:
            graph[src].append(dest)
        
        res = []
        def dfs(node):
            while node in graph and graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
            res.append(node)
        dfs('JFK')
        return res[::-1]