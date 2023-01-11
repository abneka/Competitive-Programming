class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        last_index = len(s) - 1
        
        for index, char in enumerate(s[:]):
            s[last_index - index] = char
            