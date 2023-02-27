class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref_sum = [0] * (len(s) + 1)
        
        for start, end, direction in shifts:
            if direction:
                pref_sum[start] += 1
                pref_sum[end + 1] -= 1
            
            else:
                pref_sum[start] -= 1
                pref_sum[end + 1] += 1
        
        shift = 0
        ans = ''
        
        for index, char in enumerate(s):
            shift += pref_sum[index]
            
            
            
            ans += chr((((ord(char) + shift) - 97) % 26) + 97)
        
        return ans