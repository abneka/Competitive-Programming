class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        length = len(p)
        index = 0
        ans = []
        
        anagram = Counter()
        
        for char in s:
            anagram[char] += 1
            length -= 1
            
            if length < 0:
                anagram[s[index]] -= 1
                
                if not anagram[index]:
                    del anagram[index]
                    
                length += 1
                index += 1
            
            if not length and anagram == count:
                ans.append(index)
            
        return ans