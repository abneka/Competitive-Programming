class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        equals = True
        greater = False
        
        length = len(arr)
        
        size = 1
        ans = 1
        
        for index in range(1, length):
            
            if arr[index] > arr[index - 1]:
                if  not greater and not equals:
                    size += 1
                else:
                    ans = max(ans, size)
                    size = 2
                greater = True
                equals = False
                
            elif arr[index] < arr[index - 1]:
                if greater and not equals:
                    size += 1
                else:
                    ans = max(ans, size)
                    size = 2
                greater = False
                equals = False
            
            elif arr[index] == arr[index - 1]:
                ans = max(size, ans)
                equals = True
            
        return max(ans, size)