class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        length = len(graph)
        graphs = defaultdict(list)
        for index, nodes in enumerate(graph):
            graphs[index] = nodes
        
        ans = []
        def dfs(path, index):
            if index == length - 1:
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