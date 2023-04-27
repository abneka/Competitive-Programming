class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        length = len(bombs)
        ans = 0
        graph = defaultdict(list)
        
        for index in range(length):
            for ind in range(index + 1, length):
                distance = (bombs[index][0]-bombs[ind][0])**2 + (bombs[index][1]-bombs[ind][1])**2
                
                if (bombs[index][2])**2 >= distance:
                    graph[index + 1].append(ind + 1)
                if (bombs[ind][2])**2 >= distance:
                    graph[ind + 1].append(index + 1)
        
        
        def dfs(node, visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(1, length + 1):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))
                          
        return ans