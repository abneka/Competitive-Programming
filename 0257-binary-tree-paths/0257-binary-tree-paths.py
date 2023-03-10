# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        array = []
        
        def inorderTraversal(root, path):
            if not root.left and not root.right:
                path.append(str(root.val))
                array.append('->'.join(path))
                path.pop()
                return 
                
            path.append(str(root.val))
            if root.left:
                inorderTraversal(root.left, path)
                
            if root.right:
                inorderTraversal(root.right, path)
            
            path.pop()
            
        inorderTraversal(root, [])
        
        return array