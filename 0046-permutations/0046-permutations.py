class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        
        def splitNcheck(visited, path):
            if len(path) == length:
                ans.append(path[::])
                
            for index, num in enumerate(nums):
                if visited[num]:
                    continue
                
                path.append(num)
                visited[num] += 1
                
                splitNcheck(visited, path)
                path.pop()
                visited[num] -= 1
                
        splitNcheck(Counter(), [])
        
        return ans
