class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        
        for word, count in count.items():
            heapq.heappush(heap, (-count, word))
            
        ans = [heapq.heappop(heap)[1] for _ in range(k)]
        return ans