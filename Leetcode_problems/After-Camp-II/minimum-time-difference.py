class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 24*60:
            return 0
        time = []
        ans = float('inf')
        for t in timePoints:
            h, m = map(int, t.split(':'))
            time.append((h*60) + m)

        time.sort()
        for i in range(len(time) - 1):
            ans = min(ans, abs(time[i] - time[i + 1]), abs((time[i] + 1440) - time[i + 1]))
        ans = min(ans, abs((time[0] + 1440) - time[-1]))
        return ans