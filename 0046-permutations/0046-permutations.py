class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        
        def splitNcheck(visited, path):
            if len(path) == length:
                ans.append(path[::])
                
            for index in range(length):
                if visited & (1 << index):
                    continue
                
                path.append(nums[index])
                
                splitNcheck(visited | (1 << index), path)
                path.pop()
                
        splitNcheck(0, [])
        
        return ans
