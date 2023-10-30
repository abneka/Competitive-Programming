# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to = set(to_delete)
        ans = []
        def dfs(node, push):
            nonlocal ans
            if not node:
                return None
            
            if node.val in to:
                dfs(node.left, True)
                dfs(node.right, True)
                node.left = node.right = None
                return None
            
            if push:
                ans.append(node)
            node.left = dfs(node.left, False)
            node.right = dfs(node.right, False)
            return node
        dfs(root, True)
        return ans