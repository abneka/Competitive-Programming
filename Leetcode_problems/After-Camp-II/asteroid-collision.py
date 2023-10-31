class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            if num > 0:
                stack.append(num)
                continue

            while stack and stack[-1] > 0 and stack[-1] < abs(num):
                stack.pop()
            
            if stack and stack[-1] > 0 and stack[-1] == abs(num):
                stack.pop()
                continue
            
            elif stack and stack[-1] > 0 and stack[-1] > abs(num):
                continue
            stack.append(num)
        return stack
            
