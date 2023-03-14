# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        def dfs(root, path):
            nonlocal total
            if not root.left and not root.right:
                path.append(str(root.val))
                total += int(''.join(path))
                path.pop()
                return
            
            path.append(str(root.val))
            if root.right:
                dfs(root.right, path)
            
            if root.left:
                dfs(root.left, path)
            path.pop()
        
        dfs(root, [])
        return total
    