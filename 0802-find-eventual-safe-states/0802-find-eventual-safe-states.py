class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = set()
        length = len(graph)
        g = defaultdict(list)
        
        for index, node in enumerate(graph):
            if not node:
                safe.add(index)
            g[index] = node
            
        memo = {}
        
        def dfs(node, visited):
            # if node in safe:
            #     return True
            
            if node in visited:
                return False
            
            # temp = set([node])
            visited.add(node)
            # temp.update(visited)
            
            for next_node in g[node]:
                if next_node in memo:
                    if not memo[next_node]:
                        return False
                    continue
                val = dfs(next_node, visited)
                if not val:
                    memo[node] = False
                    return val
            visited.remove(node)
            memo[node] = True
            return True
        
        ans = []
        for node in range(length):
            if dfs(node, set()):
                ans.append(node)
        
        return ans
            