class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        memo = {}
        
        def dfs(node, visited):
            memo[node] = False
            
            for next_node in graph[node]:
                if next_node in memo:
                    if not memo[next_node]:
                        return False
                    continue
                    
                if not dfs(next_node, visited):
                    memo[node] = False
                    return False
                
            memo[node] = True
            return True
        
        ans = []
        for node in range(length):
            if dfs(node, set()):
                ans.append(node)
        
        return ans
            