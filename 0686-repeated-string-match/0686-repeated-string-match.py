class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        length = len(a)
        lps = [0] * len(b)
        prev, i = 0, 1
        
        while i < len(b):
            if b[i] == b[prev]:
                lps[i] = prev + 1
                i += 1
                prev += 1
            elif not prev:
                lps[i] = 0
                i += 1
            else:
                prev = lps[prev - 1]
        
        count = 0
        j = 0
        i = 0
        while i < len(a):
            if not i:
                count += 1
            if a[i] == b[j]:
                i += 1
                i %= len(a)
                j += 1
            else:
                if not j:
                    i += 1
                elif count > 2:
                    return -1
                else:
                    j = lps[j - 1]
            if j == len(b):
                return count
        return -1