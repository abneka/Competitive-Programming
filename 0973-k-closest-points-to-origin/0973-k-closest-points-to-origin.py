class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[x**2 + y**2 , [x, y]] for x,y in points]
        points.sort()
        
        ans = []
        
        for i in range(k):
            ans.append(points[i][1])
        
        return ans
            
        