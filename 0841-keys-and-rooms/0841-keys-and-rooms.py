class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for index, room in enumerate(rooms):
            graph[index] = room
            
        visited = set()
        
        queue = deque()
        queue.append(0)
        
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            queue.extend(graph[node])
            
            visited.add(node)
        
        return len(visited) == len(rooms)