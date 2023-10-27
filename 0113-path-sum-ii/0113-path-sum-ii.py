# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, cursum, path, result):
            nonlocal targetSum
            
            if not node:
                return 
            
            cursum += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if cursum == targetSum:
                    result.append(path.copy())
                
            dfs(node.left, cursum, path, result)
            dfs(node.right, cursum, path, result)

            path.pop()
        
        result = []
        dfs(root, 0, [], result)
        return result