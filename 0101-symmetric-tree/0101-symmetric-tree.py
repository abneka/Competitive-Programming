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
        
        return self.checkSymetric(root.left, root.right)
    
    def checkSymetric(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        check_left = self.checkSymetric(left.left, right.right)
        check_right = self.checkSymetric(left.right, right.left)
        
        return check_left and left.val == right.val and check_right