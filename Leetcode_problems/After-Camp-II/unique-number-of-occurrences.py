class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occur = set(value for key, value in count.items())
        return len(occur) == len(count)