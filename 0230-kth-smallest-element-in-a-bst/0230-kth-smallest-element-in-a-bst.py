# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def createArr(root):
            if not root:
                return
            
            createArr(root.left)
            stack.append(root.val)
            createArr(root.right)
        
        createArr(root)
        return stack[k - 1]