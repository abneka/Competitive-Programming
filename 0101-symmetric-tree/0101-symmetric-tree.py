# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checkSymetric(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return checkSymetric(left.left, right.right) and left.val == right.val and checkSymetric(left.right, right.left)
        
        if not root.right and not root.left:
            return True
        
        elif not root.right or not root.left:
            return False
        
        return checkSymetric(root.left, root.right)