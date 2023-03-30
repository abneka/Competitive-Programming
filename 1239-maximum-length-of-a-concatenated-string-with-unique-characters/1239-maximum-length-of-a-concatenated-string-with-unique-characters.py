class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        length = len(arr)
        
        def splitNcheck(index, path):
            nonlocal ans
            ans = max(ans, len(path))
            
            if index == length:
                return
            
            string = set(arr[index])
                
            if len(string) == len(arr[index]) and not string & set(path):
                splitNcheck(index + 1, path + arr[index])
            
            splitNcheck(index + 1, path)
                
        splitNcheck(0, '')
        
        return ans