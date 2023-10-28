# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, par):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val * par
            
            return dfs(node.left, 1) + dfs(node.right, 0)
        
        return dfs(root, 0)