class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = re.search(needle,haystack)
        if result is None:
            return -1
        return result.start()