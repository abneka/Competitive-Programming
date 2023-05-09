class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        dep_graph = defaultdict(int)
        
        for dep, indep in prerequisites:
            graph[indep].append(dep)
            dep_graph[dep] += 1
        
        visited = set()
        queue = deque()
        
        ans = []
        
        for course in range(numCourses):
            if not dep_graph[course]:
                queue.append(course)
        
        while queue:
            node = queue.popleft()
            ans.append(node)
            visited.add(node)

            for course in graph[node]:
                dep_graph[course] -= 1
                if course not in visited and not dep_graph[course]:
                    queue.append(course)
        
        if len(visited) != numCourses:
            return []
        
        return ans
            