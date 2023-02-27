class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        path = path.split('/')
        
        for loc in path:
            if not loc:
                continue
                
            if loc[0] == '/':
                loc = loc[1:]
            
            if loc == '..':
                if stack:
                    stack.pop()
            
            elif loc == '.':
                continue
            
            else:
                stack.append(loc)
                
        return '/' + '/'.join(stack)