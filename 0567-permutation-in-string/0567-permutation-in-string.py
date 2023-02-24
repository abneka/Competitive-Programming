class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        left  = 0
        length_s2 = len(s2)
        
        permutation = Counter(s1)
        sub = s2[left:length]
        count = Counter(sub)
        
        for index in range(length, length_s2):
            if permutation == count:
                return True
            
            count[s2[index]] += 1
            count[s2[left]] -= 1
            left += 1
        
        if permutation == count:
                return True
        
        return False