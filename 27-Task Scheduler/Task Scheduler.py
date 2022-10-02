class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count =  Counter(tasks)
        count = [-c for c in count.values()]
        heapq.heapify(count)
        
        time = 0
        idle = []
        
        while count or idle:
            time += 1
            
            if count:
                c = 1 + heapq.heappop(count)
                if c:
                    idle.append([c, time + n])
            
            if idle and idle[0][1] == time:
                heapq.heappush(count, idle.pop(0)[0])
                
        return time
                
                
