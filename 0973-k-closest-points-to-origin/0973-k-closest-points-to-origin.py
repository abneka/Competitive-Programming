class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            x, y = points[i]
            points[i] = [x**2 + y**2 , [x, y]]
        # points = [[x**2 + y**2 , [x, y]] for x,y in points]
        points.sort()
        
        points = [points[i][1] for i in range(k)]
        
        # for i in range(k):
        #     ans.append(points[i][1])
        
        return points
            
        