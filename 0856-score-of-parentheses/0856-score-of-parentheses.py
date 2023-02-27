class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        total = 0
        
        for char in s:
            if char == '(':
                stack.append(total)
                total = 0
            
            else:
                if total:
                    total += stack.pop() + total
                else:
                    total += stack.pop() + 1
                    
        return total