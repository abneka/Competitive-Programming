# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val == key:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            else:
                root.val = self.inorderFinder(root.right).val
                root.right = self.deleteNode(root.right, root.val)
                
                return root
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        
        else:
            root.right = self.deleteNode(root.right, key)
            return root
    
    def inorderFinder(self, root):
        curr = root
        
        while curr.left:
            curr = curr.left
        
        return curr
        