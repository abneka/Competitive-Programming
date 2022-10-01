class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        l, r = 0, 0
        for i in range(len(tokens)):
            if tokens[i] == '+':
                r = int(result[-1])
                result.pop()
                l = int(result[-1])
                result.pop()
                result.append(l + r)
            elif tokens[i] == '-':
                r = int(result[-1])
                result.pop()
                l = int(result[-1])
                result.pop()
                result.append(l - r)
            elif tokens[i] == '*':
                r = int(result[-1])
                result.pop()
                l = int(result[-1])
                result.pop()
                result.append(l * r)
            elif tokens[i] == '/':
                r = int(result[-1])
                result.pop()
                l = int(result[-1])
                result.pop()
                result.append(l / r)
            else:
                result.append(tokens[i])
        return int(result[0])
