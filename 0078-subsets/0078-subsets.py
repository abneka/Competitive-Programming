class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        
        def dfs(index, path):
            if index == length:
                ans.append(path[::])
                return
            
            path.append(nums[index])
            dfs(index + 1, path)
            path.pop()
            dfs(index + 1, path)
            
        dfs(0, [])
        
        return ans