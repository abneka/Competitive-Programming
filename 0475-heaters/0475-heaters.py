class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            left = 0
            right = len(heaters) - 1
            radius = float('inf')
            
            while left < right:
                mid = (left + right) // 2
                
                if heaters[mid] == house:
                    radius = 0
                    break
                
                elif heaters[mid] < house:
                    radius = min(radius, house - heaters[mid])
                    left = mid + 1
                
                else:
                    radius = min(radius, heaters[mid] - house)
                    right = mid
                    
            radius = min(radius, abs(heaters[left] - house))
            ans = max(ans, radius)
            
        return ans
    
                