class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        stack = stack[:len(stack) - k]
        stack = "".join(stack)
        
        return str(int(stack)) if stack else "0"