# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            maxi = dfs(node.left) + node.val
            maxiR = dfs(node.right) + node.val

            ans = max(maxi, maxiR, maxi + (maxiR - node.val), ans, node.val)
            
            return max(maxi, maxiR, node.val)
        dfs(root)
        return ans