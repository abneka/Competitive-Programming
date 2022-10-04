class Solution:
    def calculate(self, s: str) -> int:
        stack, p, sign, total = [], 0, 1, 0
        s = s.replace(" ","")
        while p < len(s):
            char = s[p]
            if char.isdigit():
                num = ""
                while p < len(s) and s[p].isdigit():
                    num += s[p]
                    p += 1
                p -= 1
                num = int(num) *sign
                total += num
                sign = 1
            elif char in ['+', '-']:
                if stack:
                    total *= stack.pop()
                    total += stack.pop()
                if char == '-':
                    sign = -1
                stack.append(total)
                stack.append(sign)
                total, sign = 0, 1
            elif char in ['*', '/']:
                p += 1
                num = ""
                while p < len(s) and s[p].isdigit():
                    num += s[p]
                    p += 1
                p -= 1
                if char == '*':
                    total *= int(num)
                else:
                    total /= int(num)
                    total = int(total)
            p += 1
        if len(stack) == 2:
            total *= stack.pop()
            total += stack.pop()
        return int(total)