# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, depth):
            if not root:
                return (True, depth)
            
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)
            
            return (left[0] and right[0] and abs(left[1] - right[1]) < 2 , max(left[1], right[1]))
        
        return dfs(root, 0)[0]