class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count = Counter()
        final_destination = 0
        
        for people, start, end in trips:
            
            count[start] += people
            count[end] -= people
            final_destination = max(final_destination, end)
        
        for place in range(final_destination):
            capacity -= count[place]
            
            if capacity < 0:
                return False
        
        return True