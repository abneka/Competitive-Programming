# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        
        ans = []
        if not root.left:
            print(root.val)
            ans.append(root.val)
            if root.right:
                ans.extend(self.inorderTraversal(root.right))
            return ans
        
        ans.extend(self.inorderTraversal(root.left))
        ans.append(root.val)
        if root.right:
            ans.extend(self.inorderTraversal(root.right))
        return ans