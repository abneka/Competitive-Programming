# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            val = node.val if low <= node.val <= high else 0
            if low < node.val:
                val += dfs(node.left)
            if node.val < high:
                val += dfs(node.right)
            return val
        
        return dfs(root)
            