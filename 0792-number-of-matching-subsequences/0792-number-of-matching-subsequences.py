class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        memo = defaultdict(list)
        count = 0
        
        for word in words:
            memo[word[0]].append(word)            
        for char in s:
            checked = memo[char]
            memo[char] = []
            for word in checked:
                if len(word) == 1:
                    count += 1
                else:
                    memo[word[1]].append(word[1:])
        return count