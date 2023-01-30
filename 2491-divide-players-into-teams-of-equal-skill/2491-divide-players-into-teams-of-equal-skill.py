class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chemistry = 0
        
        skill.sort()
        length = len(skill)
        
        left = 0
        right = length - 1
        total = skill[0] + skill[-1]
        
        for index in range(length // 2):
            
            if total != skill[index] + skill[right - index]:
                return -1
            
            chemistry += (skill[index] * skill[right - index])
        
        return chemistry