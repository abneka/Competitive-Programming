class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        connected = [[False] * numCourses for _ in range(numCourses)]
        
        for i in range(numCourses):
            connected[i][i] = True
        
        for indep, dep in prerequisites:
            connected[indep][dep] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if connected[i][k] and connected[k][j]:
                        connected[i][j] = True
        
        return [connected[i][j] for i, j in queries]