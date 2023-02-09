class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        L=[first]
        temp = 0
        for i in encoded:
            temp = i ^ first
            L.append(temp)
            first = temp
        return L