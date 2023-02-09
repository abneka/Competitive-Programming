class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child = 0
        
        for cookie in s:
            if cookie >= g[child]:
                child += 1
                
            if child == len(g):
                return child
        
        return child