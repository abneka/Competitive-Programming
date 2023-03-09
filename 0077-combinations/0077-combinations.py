class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def combination(num, path):
            if num > n + 1:
                return
            
            if len(path) == k:
                ans.append(path[::])
                return
            
            path.append(num)
            combination(num + 1, path)
            path.pop()
            combination(num + 1, path)
            
        combination(1, [])
        return ans