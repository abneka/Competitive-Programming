class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for (start, end, val) in bookings:
            res[start-1] += val
            if end < n:
                res[end] -= val
        
        for i in range(1, n):
            res[i] += res[i-1]
            
        return res