class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        king_x, king_y = king
        y1 = y2 = x1 = x2 = d1 = d2 = d3 = d4 = -1
        
        result = []
        
        for x, y in queens:
            
            if king_x == x:
                if y - king_y > 0:
                    
                    if y1 != -1:
                        result[y1] = min(result[y1], [x, y])
                        continue
                    
                    y1 = len(result)
                else:
                    
                    if y2 != -1:
                        result[y2] = max(result[y2], [x, y])
                        continue
                    
                    y2 = len(result)
                
                result.append([x, y])
                
            elif king_y == y:
                    
                
                if x - king_x > 0:
                    
                    if x1 != -1:
                        result[x1] = min(result[x1], [x, y])
                        continue

                    x1 = len(result)
                    
                else:
                    
                    if x2 != -1:
                        result[x2] = max(result[x2], [x, y])
                        continue
                    
                    x2 = len(result)
                    
                result.append([x, y])
            
            else:
                x_diff = x - king_x
                y_diff = y - king_y
                
                if x_diff == y_diff:
                    
                    if x_diff > 0:
                        
                        if d1 != -1:
                            result[d1] = min(result[d1], [x, y])
                            continue
                        
                        d1 = len(result)
                    else:
                        
                        if d2 != -1:
                            result[d2] = max(result[d2], [x, y])
                            continue
                        
                        d2 = len(result)
                    
                    result.append([x,y])
                    
                elif x_diff == -(y_diff):
                    
                    if x_diff > 0:
                        
                        if d3 != -1:
                            result[d3] = min(result[d3], [x, y])
                            continue
                        
                        d3 = len(result)
                    else:
                        
                        if d4 != -1:
                            result[d4] = max(result[d4], [x, y])
                            continue
                        
                        d4 = len(result)
                    
                    result.append([x,y])
            
        return result