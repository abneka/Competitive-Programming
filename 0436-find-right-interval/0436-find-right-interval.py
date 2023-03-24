class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = {}
        for index, interval in enumerate(intervals):
            start[interval[0]] = index
        
        sorted_intervals = intervals[::]
        sorted_intervals.sort()
        
        result = [-1] * len(intervals)
        
        for index, interval in enumerate(intervals):
            pos = bisect_left(sorted_intervals, [interval[1], -float('inf')])
            if pos != len(intervals):
                result[index] = start[sorted_intervals[pos][0]]
        
        return result