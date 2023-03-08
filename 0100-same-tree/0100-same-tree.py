# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p:
            return False
        
        if not q:
            return False
        
        return self.isSameTree(p.right, q.right) and q.val == p.val and self.isSameTree(p.left, q.left)