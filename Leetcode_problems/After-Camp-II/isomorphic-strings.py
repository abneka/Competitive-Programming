class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap = defaultdict(int)
        hmap2 = defaultdict(int)

        for i in range(len(s)):
            if hmap[s[i]]:
                if hmap[s[i]] == hmap2[t[i]]:
                    continue
                else:
                    return False
            if hmap2[t[i]]:
                return False
            
            hmap[s[i]] = i + 1
            hmap2[t[i]] = i + 1

        return True if hmap[s[-1]] == hmap2[t[-1]] else False