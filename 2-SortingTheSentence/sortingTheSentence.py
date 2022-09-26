class Solution:
    def sortSentence(self, s: str) -> str:
        spli = s.split(' ')
        res = ''
        counter = 0
        for y in spli:
            counter += 1
            for s in spli:
                if (s[-1] == str(counter)):
                    res += s.replace(str(counter), ' ')
                    break
        return res.strip()
