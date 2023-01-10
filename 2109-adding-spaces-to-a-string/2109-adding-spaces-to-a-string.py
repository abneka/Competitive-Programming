class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ''
        offset = 0
        space_index = 0
        space_size = len(spaces)
        
        for index, char in enumerate(s):
            if space_size == space_index:
                result = result + s[index:]
                break
            
            if index == spaces[space_index]:
                result += ' '
                offset += 1
                space_index += 1
            
            result += char
            
        return result