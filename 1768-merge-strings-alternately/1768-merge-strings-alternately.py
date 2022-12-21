class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        high = max(len1, len2)
        string = ''
        for i in range(high):
            if i < len1:
                string = string + word1[i]
            if i < len2:
                string = string + word2[i]
                
        return string