"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        importance = defaultdict(int)
        
        for emp in employees:
            graph[emp.id] = emp.subordinates
            importance[emp.id] = emp.importance

        def dfs(id):
            
            total = importance[id]
            for ids in graph[id]:
                total += dfs(ids)
            
            return total
         
        return dfs(id)
        
        