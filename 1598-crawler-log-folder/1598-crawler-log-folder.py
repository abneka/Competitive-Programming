class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for path in logs:
            if path == '../':
                if count:
                    count -= 1
            
            elif path == './':
                continue
            
            else:
                count += 1
            
        return count