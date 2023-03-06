class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words = self.freq(words)
        queries = self.freq(queries)
        
        words.sort()
        length = len(words)
        
        for index, size in enumerate(queries):
            queries[index] = length - self.searchInsert(words, size)
                
        return queries
    
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        mid = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] < target:
                low = mid + 1
                
            elif nums[mid] > target:
                high = mid - 1
                
            else:
                low = mid + 1
                mid += 1
        
        if mid < len(nums) and nums[mid] < target:
            return mid + 1
        
        return mid
    
    def freq(self, words):
        ans = []
        for index, word in enumerate(words):
            word = sorted(word)
            char = word[0]
            
            word = Counter(word)
            ans.append(word[char])
            
        return ans