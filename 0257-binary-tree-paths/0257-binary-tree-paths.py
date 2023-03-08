# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        array = []
        
        def inorderTraversal(root, string):
            if not root.left and not root.right:
                string += str(root.val)
                array.append(string)
                
            string += str(root.val) + '->'
            if root.left:
                inorderTraversal(root.left, string)
                
            if root.right:
                inorderTraversal(root.right, string)

        inorderTraversal(root, '')
        
        return array