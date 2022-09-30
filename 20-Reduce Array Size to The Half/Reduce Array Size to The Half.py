class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count =  Counter(arr)
        freq = sorted(count.values(), reverse=True)
        half = int(len(arr)/2)
        result = 0
        while half > 0:
            half -= freq[result]
            result += 1
        return result
