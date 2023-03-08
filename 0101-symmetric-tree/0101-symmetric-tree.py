# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left:
            return True
        
        elif not root.right or not root.left:
            return False
        
        return self.check(root.left, root.right)
    
    def check(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return self.check(left.left, right.right) and left.val == right.val and self.check(left.right, right.left)