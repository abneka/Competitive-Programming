class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(index, path):
            if index == len(nums):
                if path in ans:
                    return
                
                if len(path) > 1:
                    ans.append(path[::])
                return
            
            if not path or nums[index] >= path[-1]:
                path.append(nums[index])
                backtrack(index + 1, path)
                path.pop()
            backtrack(index + 1, path)
                
        backtrack(0, [])
        
        return ans