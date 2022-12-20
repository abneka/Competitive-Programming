class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        l, r = 0, len(string)-1
        
        while l < r:
            if string[l] != string[r]:
                return False
            l = l+1
            r = r-1

        return True
