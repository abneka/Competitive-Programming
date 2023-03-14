# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, root, curr):
        if not root:
            return 0
        
        curr = curr * 10 + root.val
        if not root.left and not root.right:
            return curr
        
        return self.dfs(root.left, curr) + self.dfs(root.right, curr)