# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def merge(a, b):
            if not a:
                return b
            if not b:
                return a
            
            curr = b
            while curr.left:
                curr = curr.left
            curr.left = a
            return b
        def dfs(node):
            if not node:
                return None
            
            if node.val == key:
                return merge(node.left, node.right)
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        return dfs(root)