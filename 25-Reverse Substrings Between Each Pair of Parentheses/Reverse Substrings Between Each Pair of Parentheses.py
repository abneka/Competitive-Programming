class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        
        for char in s:
            if char == '(':
                stack.append('')
            elif char == ')':
                word = stack.pop()[::-1]
                stack[-1] += word
            else:
                stack[-1] += char
        
        return stack[0]
