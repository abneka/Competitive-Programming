class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center = set(edges[0])
        for edge in edges:
            center = center & set(edge)
        
        return list(center)[0]