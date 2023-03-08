# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxi = 0
        
        def depthFirst(root):
            nonlocal maxi
            left, right = 0,0
            if root.left:
                left = depthFirst(root.left)
            
            if root.right:
                right = depthFirst(root.right)
                
            if root.left and root.right and root.val == root.left.val and root.val == root.right.val:
                maxi = max(maxi, 2 + left + right)
                return 1 + max(left, right)
            
            elif root.left and root.left.val == root.val:
                maxi = max(maxi, 1 + left)
                return 1 + left
            
            elif root.right and root.right.val == root.val:
                maxi = max(maxi, 1 + right)
                return 1 + right
            
            else:
                return 0
        
        depthFirst(root)
        return maxi