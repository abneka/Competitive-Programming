class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words = self.freq(words)
        queries = self.freq(queries)
        
        words.sort()
        length = len(words)
        
        def searchInsert():
            low = 0
            high = len(words) - 1
            mid = 0

            while low <= high:
                mid = (low + high) // 2

                if words[mid] < size:
                    low = mid + 1

                elif words[mid] > size:
                    high = mid - 1

                else:
                    low = mid + 1
                    mid += 1

            if mid < len(words) and words[mid] < size:
                return mid + 1

            return mid
        
        for index, size in enumerate(queries):
            queries[index] = length - searchInsert()
                
        return queries
    
    def freq(self, words):
        ans = []
        for index, word in enumerate(words):
            word = sorted(word)
            char = word[0]
            
            word = Counter(word)
            ans.append(word[char])
            
        return ans