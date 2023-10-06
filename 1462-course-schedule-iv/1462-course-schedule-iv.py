class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        outdeg = defaultdict(int)
        pre = [set() for _ in range(numCourses)]
        
        for indep, dep in prerequisites:
            graph[dep].append(indep)
            outdeg[indep] += 1
            
        queue = deque()
        
        for node in range(numCourses):
            if not outdeg[node]:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            
            for course in graph[node]:
                pre[course].add(node)
                pre[course].update(pre[node])
                
                outdeg[course] -= 1
                
                if not outdeg[course]:
                    queue.append(course)
        
        return [dep in pre[indep] for indep, dep in queries]