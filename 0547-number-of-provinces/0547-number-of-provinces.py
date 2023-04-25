class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        length = len(isConnected)
        
        def dfs(isConnected, visited, city_a):
            if city_a in visited:
                return 0
            
            visited.add(city_a)
            
            for city_b in range(length):
                if isConnected[city_a][city_b]:
                    dfs(isConnected, visited, city_b)
            return 1
        
        prov = 0
        
        for city_a in range(length):
            prov += dfs(isConnected, visited, city_a)
        return prov