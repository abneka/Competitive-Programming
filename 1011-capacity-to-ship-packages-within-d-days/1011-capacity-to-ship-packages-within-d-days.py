class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right = sum(weights)
        
        res = right
        
        while left <= right:
            capacity = (left + right) // 2
            
            total = 0
            count = 0
            
            for weight in weights:
                if weight > capacity:
                    count = days + 1
                    break
                    
                if total + weight > capacity:
                    count += 1
                    total = 0
                total += weight
            
            if total:
                count += 1
            
            if count <= days:
                res = min(res, capacity)
                right = capacity - 1
            
            else:
                left = capacity + 1
        
        return res