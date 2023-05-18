class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        pre = [set() for _ in range(numCourses)]
        
        for dep, indep in prerequisites:
            graph[indep].append(dep)
            indeg[dep] += 1
            
        queue = deque()
        
        for node in range(numCourses):
            if not indeg[node]:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            
            for course in graph[node]:
                pre[course].add(node)
                pre[course].update(pre[node])
                
                indeg[course] -= 1
                
                if not indeg[course]:
                    queue.append(course)
        
        return [dep in pre[indep] for indep, dep in queries]