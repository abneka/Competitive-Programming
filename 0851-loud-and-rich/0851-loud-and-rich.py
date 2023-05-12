class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        length = len(quiet)
        ans = [-1] * length
        compare = lambda a, b: a if quiet[a] < quiet[b] else b
        
        for rich, poor in richer:
            graph[poor].append(rich)
        
        def dfs(node):
            if ans[node] + 1:
                return ans[node]
            
            mini = node
            for next_node in  graph[node]:
                mini = compare(mini, dfs(next_node))
            
            ans[node] = mini
            return mini
        
        for index in range(length):
            ans[index] = dfs(index)
        
        return ans