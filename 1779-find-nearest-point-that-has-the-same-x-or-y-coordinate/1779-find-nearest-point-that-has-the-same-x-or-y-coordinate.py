class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        manhattan = [float('inf'), -1]
        for index, cord in enumerate(points):
            if cord[0] == x or cord[1] == y:
                distance = abs(cord[0] - x) + abs(cord[1] - y)
                if distance < manhattan[0]:
                    manhattan = [distance, index]
                
        return manhattan[1]