class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1 = len(word1)
        length2 = len(word2)
        
        @cache
        def dp(ind1, ind2):
            if ind1 == length1 or ind2 == length2:
                return max(length1 - ind1, length2 - ind2)
            
            if word1[ind1] == word2[ind2]:
                return dp(ind1 + 1, ind2 + 1)
            
            remove = 1 + dp(ind1 + 1, ind2)
            replace = 1 + dp(ind1 + 1, ind2 + 1)
            add = 1 + dp(ind1, ind2 + 1)
            return min(remove, replace, add)
        
        return dp(0 , 0)