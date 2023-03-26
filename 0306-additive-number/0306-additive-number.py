class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(start, arr):
            if len(arr) >= 3 and arr[-1] != arr[-2] + arr[-3]:
                return False
            if start == len(num) and len(arr) >= 3:
                return True
            for i in range(start, len(num)):
                if num[start] == '0' and i > start:
                    break
                curr = int(num[start:i+1])
                if len(arr) < 2 or curr == arr[-1] + arr[-2]:
                    if backtrack(i+1, arr + [curr]):
                        return True
            return False
        
        return backtrack(0, [])