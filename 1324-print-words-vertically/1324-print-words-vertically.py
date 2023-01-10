class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        sizes = {}
        max_size = 0
        last_word = s[len(s)-1]
        result = []
        
        for index, word in enumerate(s):
            sizes[index] = len(word)
            max_size = max(sizes[index], max_size)
        
        for index in range(max_size):
            element = ''
            
            for order, word in enumerate(s):
                if index < sizes[order]:
                    element += word[index]
                else:
                    element += ' '
            
            element = element.rstrip()
            result.append(element)
            
        return result
            