class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        stack =  []
        res = 0
        while r < len(s):
            while stack and s[r] in stack:
                stack.pop(0)
                l += 1
            stack.append(s[r])
            res = max(res, len(stack))
            r += 1
        return res
        