# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def createGst(root, val):
            if not root:
                return val

            right = createGst(root.right, val)
            
            root.val += right
            left = 0
            if root.left:
                left = createGst(root.left, root.val)
                
            return max(root.val, left)
            
        createGst(root, 0)
        return root