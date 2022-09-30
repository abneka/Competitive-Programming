class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        count = list(freq.keys())
        count = count[:k]
        return count
