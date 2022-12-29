class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # res = sorted(points, key=lambda point: point[0]**2+point[1]**2)
        points.sort(key = lambda point: point[0]**2+point[1]**2)
        return points[:k]