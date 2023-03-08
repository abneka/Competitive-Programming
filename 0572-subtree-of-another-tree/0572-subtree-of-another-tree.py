# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root.val == subRoot.val:
            return self.isSubtree(root.left, subRoot)or self.checkTree(root, subRoot) or self.isSubtree(root.right, subRoot)
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def checkTree(self, root1, root2):
        if not root1 and not root2:
            return True
        
        elif not root1:
            return False
        
        elif not root2:
            return False
        
        return self.checkTree(root1.right, root2.right) and root2.val == root1.val and self.checkTree(root1.left, root2.left)