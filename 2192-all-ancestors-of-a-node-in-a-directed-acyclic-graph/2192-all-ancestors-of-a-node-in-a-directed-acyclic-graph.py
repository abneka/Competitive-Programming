class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> Iterable[List[int]]:
        graph = defaultdict(set)
        
        for parent, child in edges:
            graph[child].add(parent)

        memo = [set() for _ in range(n)]
        
        def dfs(parent):
            if not memo[parent]:
                for child in graph[parent]:
                    if child not in memo[parent]:
                        memo[parent].update({child})
                        memo[parent].update(dfs(child))
            return memo[parent]

        for parent in range(n):
            if not memo[parent]:
                dfs(parent)

        return map(sorted, memo)