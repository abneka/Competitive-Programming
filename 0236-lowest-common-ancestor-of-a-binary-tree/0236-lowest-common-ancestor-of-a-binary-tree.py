# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findAncestor(root):
            if not root:
                return (0, False)

            if root.val == p.val or root.val == q.val:
                return (root, True)

            left = findAncestor(root.left)
            right = findAncestor(root.right)

            if left[1] and right[1]:
                return (root, True)

            elif left[1]:
                return left

            return right
        
        return findAncestor(root)[0]
        