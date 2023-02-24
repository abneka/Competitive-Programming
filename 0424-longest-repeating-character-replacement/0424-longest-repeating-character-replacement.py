class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maximum_freq = 0
        left = 0
        
        count = Counter()
        
        for right, char in enumerate(s):
            count[char] += 1
            maximum_freq = max(maximum_freq, count[char])
            
            window_size = right - left + 1
            
            if window_size > maximum_freq + k:
                count[s[left]] -= 1
                left += 1
        
        return len(s) - left