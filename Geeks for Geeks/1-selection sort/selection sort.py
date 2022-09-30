class Solution: 
    def select(self, arr, i):
        minimum = float('inf')
        for i in range(i, len(arr)):
            minimum = min(minimum, arr[i])
        return minimum
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)-1):
            mini = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i] , arr[mini] = arr[mini], arr[i]
        
        return arr
