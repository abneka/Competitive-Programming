class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c:i for i, c in enumerate(s)}
        stack =[]
        
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and c < stack[-1] and last[stack[-1]] > i:
                stack.pop()
            stack.append(c)
            
        return ''.join(stack)