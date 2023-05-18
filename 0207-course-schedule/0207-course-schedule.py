class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        
        for dep, indep in prerequisites:
            graph[indep].append(dep)
            indeg[dep] += 1
        
        queue = deque()
        visited = set()
        
        for node in range(numCourses):
            if not indeg[node]:
                queue.append(node)
                
        while queue:
            node = queue.popleft()
            visited.add(node)
            
            for course in graph[node]:
                indeg[course] -= 1
                if not indeg[course] and course not in visited:
                    queue.append(course)
            
        if len(visited) == numCourses:
            return True
        return False