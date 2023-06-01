class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = [0] * (n + 1)
        if not n:
            return 0
        arr[1] = 1
        maxi = 1
        
        for i in range(2, n + 1):
            half = i // 2
            new = 0
            if i % 2:
                new = arr[half] + arr[half + 1]
            else:
                new = arr[half]
            arr[i] = new
            maxi = max(maxi, new)
            
        return maxi
