class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n:
            return 0
        
        arr = [0] * (n + 1)
        arr[1] = 1
        maxi = 1
        
        for index in range(2, n + 1):
            half = index // 2
            if index % 2:
                arr[index] = arr[half] + arr[half + 1]
            else:
                arr[index] = arr[half]
            maxi = max(arr[index], maxi)
        
        return maxi