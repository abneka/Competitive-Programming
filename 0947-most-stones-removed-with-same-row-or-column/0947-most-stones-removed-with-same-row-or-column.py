class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row = defaultdict(list)
        col = defaultdict(list)
        
        for x, y in stones:
            row[x].append(y)
            col[y].append(x)
            
        neigh = 0
        visited = set()
        
        for x, y in stones:
            if (x, y) not in visited:
                queue = deque()
                queue.append((x, y))
                
                while queue:
                    stone_x, stone_y = queue.popleft()
                    
                    if (stone_x, stone_y) not in visited:
                        visited.add((stone_x, stone_y))
                        
                        for y in row[stone_x]:
                            queue.append([stone_x, y])
                            
                        for x in col[stone_y]:
                            queue.append([x, stone_y])
                neigh += 1
        
        return len(stones) - neigh