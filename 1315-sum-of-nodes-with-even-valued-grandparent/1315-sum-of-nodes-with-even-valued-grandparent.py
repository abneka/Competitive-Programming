# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        
        def traverse(root):
            nonlocal total
            if not root:
                return None
            
            if not root.val % 2:
                total += self.addGrandchilds(root.left, False) + self.addGrandchilds(root.right, False)
                
            traverse(root.right)
            traverse(root.left)
        
        traverse(root)
            
        return total
         
    def addGrandchilds(self, root, Grand):
        if not root:
            return 0
        
        if not Grand:
            return self.addGrandchilds(root.left, not Grand) + self.addGrandchilds(root.right, not Grand)
        
        return root.val