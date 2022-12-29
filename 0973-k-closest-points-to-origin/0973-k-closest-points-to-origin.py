class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = [[x**2 + y**2 , [x, y]] for x,y in points]
        result.sort()
        
        ans = []
        
        for i in range(k):
            ans.append(result[i][1])
        
        return ans
            
        