class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        queue = deque()
        visited = set([(0,1)])
        
        if source == target:
            return 0
        
        path = defaultdict(list)
        buses = defaultdict(list)
        
        for b, bus in enumerate(routes):
            buses[b] = bus
            for r, route in enumerate(bus):
                path[route].append(b)
        
        for start in path[source]:
            visited.add(start)
            queue.extend(buses[start])
            
        count = 1
            
        while queue:
            for _ in range(len(queue)):
                pos = queue.popleft()
                
                if pos == target:
                    return count
                
                for next_bus in path[pos]:
                    if next_bus not in visited:
                        visited.add(next_bus)
                        queue.extend(buses[next_bus])
            
            count += 1
        return -1
            