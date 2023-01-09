class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = [] 
        buffer = ''
        skip_characters = False
        
        for line in source:
            index = 0
            while index < len(line):
                char = line[index]
                
                # "//" -> Line comment.
                if char == '/' and (index + 1) < len(line) and line[index + 1] == '/' and not skip_characters:
                    break 
                    
                # "/*" -> Start of block comment.
                elif char == '/' and (index + 1) < len(line) and line[index + 1] == '*' and not skip_characters:
                    skip_characters = True
                    index += 1
                    
                # "*/" -> End of block comment.
                elif char == '*' and (index + 1) < len(line) and line[index + 1] == '/' and skip_characters:
                    skip_characters = False
                    index += 1
                    
                # Normal character. Append to buffer if not in block comment.
                elif not skip_characters:
                    buffer += char
                    
                index += 1
            if buffer and not skip_characters:
                result.append(buffer)
                buffer = ''
                
        return result