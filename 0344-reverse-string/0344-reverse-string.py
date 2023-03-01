class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l = 0
        r = len(s) - 1
        
        def reverse(left, right):
            if left >= right:
                return 
            
            s[left], s[right] = s[right], s[left]
            reverse(left + 1, right - 1)
        
        reverse(l, r)
        
#         last_index = len(s) - 1
        
#         for index, char in enumerate(s[:]):
#             s[last_index - index] = char
            
