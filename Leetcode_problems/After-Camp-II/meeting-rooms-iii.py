class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [i for i in range(n)]
        heap = []
        count = defaultdict(int)
        currTime = 0

        for start, end in meetings:
            duration = end - start
            currTime = max(start, currTime)
            if not rooms:
                currTime = max(currTime, heap[0][0])
            
            while heap and heap[0][0] <= currTime:
                heappush(rooms, heappop(heap)[1])

            currRoom = heapq.heappop(rooms)
            count[currRoom] += 1
            heapq.heappush(heap, (currTime + duration, currRoom))
        
        
        maxi = 0
        ans = 0
        for room in count:
            if count[room] > maxi:
                maxi = count[room]
                ans = room
        return ans