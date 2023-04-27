class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        length = len(bombs)
        graph = defaultdict(list)
        
        for index in range(length):
            for ind in range(index + 1, length):
                distance = sqrt((bombs[index][0]-bombs[ind][0])**2 + (bombs[index][1]-bombs[ind][1])**2)
                
                if bombs[index][2] >= distance:
                    graph[index + 1].append(ind + 1)
                if bombs[ind][2] >= distance:
                    graph[ind + 1].append(index + 1)
                    
        
        def depth(start, visited):
            if start in visited:
                return 0

            visited.append(start)
            detonate = 1
            
            for child in graph[start]:
                if child not in visited:
                    detonate += depth(child, visited)
            
            return detonate
        
        result = 1
        for start in range(1, length + 1):
            result = max(result, depth(start, []))
        
        return result