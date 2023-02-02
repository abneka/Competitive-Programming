class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        length1 =len(word1)
        length2 = len(word2)
        length = length1 + length2
        
        char1 = 0
        char2 = 0
        
        merge = ''
        cache = ''
        count = 0
        is_equal = False
        
        while char1 < length1 and char2 < length2:
            
            
            
            if word1[char1] > word2[char2]:
                merge += word1[char1]
                char1 += 1
            
            elif word1[char1] < word2[char2]:
                merge += word2[char2]
                char2 += 1
            
            else:
                
                if word1[char1:] == word2[char2:]:
                    is_equal = True
                    # continue
                    
                if is_equal:
                    merge += word1[char1]
                    is_equal = False
                    char1 += 1
                    continue
                
                count = 0
                while word1[char1: char1 + count] == word2[char2: char2 + count]:
                    count += 1
                    if char1 + count == length1 or char2 + count == length2:
                        break
                        
                if word1[char1: char1 + count] > word2[char2: char2 + count]:
                    merge += word1[char1]
                    char1 += 1
                    
                elif word1[char1: char1 + count] < word2[char2: char2 + count]:
                    merge += word2[char2]
                    char2 += 1
                
                else:
                    if char1 + count == length1:
                        merge += word2[char2]
                        char2 += 1
                    elif char2 + count == length2:
                        merge += word1[char1]
                        char1 += 1
                    
        if char2 == length2:
            merge += word1[char1:]
            
        if char1 == length1:
            merge += word2[char2:]
        
        
        return merge