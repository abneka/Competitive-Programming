class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
            
        res = []
        count, end = 0, 0
        
        for i, c in enumerate(s):
            count +=1
            end = max (end, lastIndex[c])
            
            if end == i:
                res.append(count)
                count = 0
                
        return res