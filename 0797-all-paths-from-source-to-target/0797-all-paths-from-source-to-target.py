class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graphs = defaultdict(list)
        maximum = 0
        for index, nodes in enumerate(graph):
            graphs[index] = nodes
            if nodes:
                maximum = max(max(nodes), maximum)
        
        ans = []
        def dfs(path, index):
            if index == maximum:
                path.append(index)
                ans.append(path[::])
                path.pop()
                return
            
            path.append(index)
            
            for ind in graphs[index]:
                dfs(path, ind)
            path.pop()
        
        dfs([], 0)
        return ans