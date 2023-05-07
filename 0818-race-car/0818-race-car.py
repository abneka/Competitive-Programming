class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1)])
        visited = set([(0,1)])
        path = 0
        
        while queue:
            for _ in range(len(queue)):
                position,speed = queue.popleft()
                if position == target:
                    return path
                
                if(position + speed, speed * 2) not in visited:
                    queue.append((position + speed, speed * 2))
                    visited.add((position + speed, speed * 2))
                    
                if speed > 0 and (position, -1) not in visited:
                    queue.append((position, -1))
                    visited.add((position, -1))
                elif speed <= 0 and (position, 1) not in visited:
                    queue.append((position, 1))
                    visited.add((position, 1))
           
            path += 1
        return -1